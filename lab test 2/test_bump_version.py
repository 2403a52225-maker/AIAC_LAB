# test_bump_version.py
import pytest
from bump_version import bump_version

@pytest.mark.parametrize("input_name,expected", [
    ('report_v1.csv', 'report_v02.csv'),
    ('summary.csv', 'summary_v01.csv'),
    ('log_v09.txt', 'log_v10.txt'),
    ('archive.tar.gz', 'archive_v01.tar.gz'),
    ('backup_v99.tar.gz', 'backup_v100.tar.gz'),
    ('multi.part.name_v9.txt', 'multi.part.name_v10.txt'),
    ('noext', 'noext_v01'),
    ('.env', '.env_v01'),
    ('weird_v009.log', 'weird_v010.log'),
    ('prefix_v1_other.csv', 'prefix_v1_other_v01.csv'),  # ensure only trailing _vN matches
    ('Report_V2.csv', 'Report_V03.csv'),  # preserve V case
])
def test_bump_cases(input_name, expected):
    assert bump_version(input_name) == expected
