from gepwc.core import gepcat
from click.testing import CliRunner
def test_gepcat():
    runner = CliRunner()
    result = runner.invoke(gepcat,['hello world'])
    assert result.exit_code == 0
    assert result.output == 'hello world\n'
