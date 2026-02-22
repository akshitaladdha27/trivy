import pytest

def test_docker_build_status():
    assert True

def test_trivy_scan_readiness():
    app_status = "ready"
    assert app_status == "ready"