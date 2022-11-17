
import pytest





pytest.main(['-vs', './testcase/test_application.py', '--alluredir=./report/html', '--clean-alluredir','-p' 'no:warnings'])





