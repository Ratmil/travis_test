import openerp.tests
import logging

_logger = logging.getLogger(__name__)


@openerp.tests.common.at_install(False)
@openerp.tests.common.post_install(True)
class TestTravisTest(openerp.tests.common.TransactionCase):
    def test_1(self):
        self.assertTrue(False)
       
