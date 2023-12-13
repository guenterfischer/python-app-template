import subprocess


def test_about():
    result = subprocess.run(
        "pyapp about", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )

    assert 0 == result.returncode
    assert 0 == len(result.stderr)
