"""Device handler for Trust ZYCT-202 remote."""
from zigpy.profiles import zha
from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.general import Basic, Groups, Identify, LevelControl

from zhaquirks.const import (
    ARGS,
    CLUSTER_ID,
    COMMAND_MOVE,
    COMMAND_OFF_WITH_EFFECT,
    COMMAND_ON,
    COMMAND,
    DEVICE_TYPE,
    DIM_DOWN,
    DIM_UP,
    ENDPOINT_ID,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
    SHORT_PRESS,
    TURN_OFF,
    TURN_ON,
)

MANUFACTURER_SPECIFIC_CLUSTER_ID = 0x1000


class TrustZYCT202(CustomDevice):
    """Trust ZYCT-202."""

    signature = {
        # <SimpleDescriptor endpoint=1 profile=49246 device_type=2080
        # device_version=2
        # input_clusters=[0, 4, 3, 6, 8, 4096]
        # output_clusters=[0, 4, 3, 6, 8, 4096]>
        MODELS_INFO: [("TRUST", "ZYCT-202 Remote")],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.REMOTE_CONTROL,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    LevelControl.cluster_id,
                    MANUFACTURER_SPECIFIC_CLUSTER_ID,
                ],
                OUTPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    LevelControl.cluster_id,
                    MANUFACTURER_SPECIFIC_CLUSTER_ID,
                ],
            }
        },
    }

    replacement = {
        1: {
            PROFILE_ID: zha.PROFILE_ID,
            DEVICE_TYPE: zha.DeviceType.REMOTE_CONTROL,
            INPUT_CLUSTERS: [
                Basic.cluster_id,
                Identify.cluster_id,
                Groups.cluster_id,
                LevelControl.cluster_id,
                MANUFACTURER_SPECIFIC_CLUSTER_ID,
            ],
            OUTPUT_CLUSTERS: [
                Basic.cluster_id,
                Identify.cluster_id,
                Groups.cluster_id,
                LevelControl.cluster_id,
                MANUFACTURER_SPECIFIC_CLUSTER_ID,
            ],
        }
    }

    device_automation_triggers = {
        (SHORT_PRESS, TURN_ON): {COMMAND: COMMAND_ON, CLUSTER_ID: 6, ENDPOINT_ID: 1},
        (SHORT_PRESS, DIM_UP): {
            COMMAND: COMMAND_MOVE,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 1,
            ARGS: [0, 30],
        },
        (SHORT_PRESS, DIM_DOWN): {
            COMMAND: COMMAND_MOVE,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 1,
            ARGS: [1, 30],
        },
        (SHORT_PRESS, TURN_OFF): {
            COMMAND: COMMAND_OFF_WITH_EFFECT,
            CLUSTER_ID: 6,
            ENDPOINT_ID: 1,
        },
    }
