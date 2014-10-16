
"""
This is the testing unit for MUSiCC
"""
# to comply with both Py2 and Py3
from __future__ import absolute_import, division, print_function

import unittest
import filecmp
import MUSiCC
import os
import pandas as pd


class MUSiCCTestCase(unittest.TestCase):
    """Tests for `MUSiCC.py`."""

    def test_is_output_correct_for_normalization_only(self):
        """Does MUSiCC produce the correct output for normalization of the example case?"""
        # define the arguments needed by MUSiCC
        musicc_args = {'input_file': 'examples/simulated_ko_relative_abundance.tab',
                       'output_file': 'examples/test1.tab', 'input_format': 'tab', 'output_format': 'tab', 'MUSiCC_inter': True,
                       'MUSiCC_intra': 'None', 'compute_scores': True, 'verbose': False}
        # run the MUSiCC correction
        MUSiCC.correct(musicc_args)
        # assert that the result is equal to the example
        self.assertTrue(filecmp.cmp('examples/test1.tab', 'examples/simulated_ko_MUSiCC_Normalized.tab'))
        os.remove('examples/test1.tab')

    def test_is_output_correct_for_normalization_correction_use_generic(self):
        """Does MUSiCC produce the correct output for normalization and correction of the example case?"""
        # define the arguments needed by MUSiCC
        musicc_args = {'input_file': 'examples/simulated_ko_relative_abundance.tab',
                       'output_file': 'examples/test2.tab', 'input_format': 'tab', 'output_format': 'tab', 'MUSiCC_inter': True,
                       'MUSiCC_intra': 'use_generic', 'compute_scores': True, 'verbose': False}
        # run the MUSiCC correction
        MUSiCC.correct(musicc_args)
        # assert that the result is equal to the example
        self.assertTrue(filecmp.cmp('examples/test2.tab', 'examples/simulated_ko_MUSiCC_Normalized_Corrected_use_generic.tab'))
        os.remove('examples/test2.tab')

    def test_is_output_correct_for_normalization_correction_learn_model(self):
        """Does MUSiCC produce the correct output for normalization and correction of the example case?"""
        # define the arguments needed by MUSiCC
        musicc_args = {'input_file': 'examples/simulated_ko_relative_abundance.tab',
                       'output_file': 'examples/test3.tab', 'input_format': 'tab', 'output_format': 'tab', 'MUSiCC_inter': True,
                       'MUSiCC_intra': 'learn_model', 'compute_scores': True, 'verbose': False}
        # run the MUSiCC correction
        MUSiCC.correct(musicc_args)
        # assert that the result is equal to the example
        example = pd.read_table('examples/simulated_ko_MUSiCC_Normalized_Corrected_learn_model.tab', index_col=0)
        output = pd.read_table('examples/test3.tab', index_col=0)
        example_vals = example.values
        output_vals = output.values
        self.assertTrue(example_vals.shape[0] == output_vals.shape[0])
        self.assertTrue(example_vals.shape[1] == output_vals.shape[1])
        # since this is de novo learning, results may vary when testing, so
        # check that output values are not very far from the expected example values
        for i in range(example_vals.shape[0]):
            for j in range(example_vals.shape[1]):
                self.assertTrue(abs(example_vals[i, j] - output_vals[i, j]) < 1)

        os.remove('examples/test3.tab')

################################################

if __name__ == '__main__':
    unittest.main()

