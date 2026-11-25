import pytest
import imaging.rgbd_depth as mod

CASES = [
    ("rgbd_time_align", (1,)),
    ("hole_confidence_propagate", (1,)),
    ("edge_aware_guide", (1,)),
    ("motion_mask_reproject", (1,)),
    ("block_boundary_constraint", (1,)),
    ("cache_key_intrinsic", (1,)),
    ("load_rgbd", (1,)),
    ("complete_depth", (1,)),
    ("fuse_depth_frames", (1,)),
    ("present_rgbd", (1,)),
    ("validate_rgbd", (1,)),
    ("metrics_rgbd", (1,)),
    ("audit_rgbd", (1,)),
    ("fallback_rgbd", (1,)),
    ("determinism_rgbd", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
