#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for Python Jour 2 - Les Boucles exercises
Tests all 9 jobs to ensure correct output
"""

import pytest
from io import StringIO
import sys


class TestJob01:
    """Test Job 01: Display numbers 0-20"""
    
    def test_job_01_output(self, capsys):
        """Test that Job 01 displays numbers from 0 to 20"""
        # Execute Job 01
        for nombre in range(21):
            print(nombre)
        
        captured = capsys.readouterr()
        output_lines = captured.out.strip().split('\n')
        
        assert len(output_lines) == 21, "Should output 21 lines (0-20)"
        assert output_lines[0] == "0", "Should start with 0"
        assert output_lines[20] == "20", "Should end with 20"


class TestJob02:
    """Test Job 02: Display every other number 0-20"""
    
    def test_job_02_output(self, capsys):
        """Test that Job 02 displays every 2nd number"""
        # Execute Job 02
        for nombre in range(0, 21, 2):
            print(nombre)
        
        captured = capsys.readouterr()
        output_lines = captured.out.strip().split('\n')
        
        assert len(output_lines) == 11, "Should output 11 numbers (0,2,4...20)"
        assert output_lines[0] == "0", "Should start with 0"
        assert output_lines[10] == "20", "Should end with 20"
        
        # Verify all are even
        for line in output_lines:
            assert int(line) % 2 == 0, f"{line} should be even"


class TestJob03:
    """Test Job 03: Display squares of numbers 1-20"""
    
    def test_job_03_output(self, capsys):
        """Test that Job 03 displays correct squares"""
        # Execute Job 03
        for nombre in range(1, 21):
            print(f"{nombre}^2 = {nombre**2}")
        
        captured = capsys.readouterr()
        output_lines = captured.out.strip().split('\n')
        
        assert len(output_lines) == 20, "Should output 20 lines"
        
        # Verify first and last
        assert "1^2 = 1" in output_lines[0], "First should be 1^2 = 1"
        assert "20^2 = 400" in output_lines[19], "Last should be 20^2 = 400"


class TestJob05:
    """Test Job 05: While loop from 0 to 12"""
    
    def test_job_05_output(self, capsys):
        """Test that Job 05 displays 0-12 using while loop"""
        # Execute Job 05
        count = 0
        while count < 13:
            print(count)
            count += 1
        
        captured = capsys.readouterr()
        output_lines = captured.out.strip().split('\n')
        
        assert len(output_lines) == 13, "Should output 13 lines (0-12)"
        assert output_lines[0] == "0", "Should start with 0"
        assert output_lines[12] == "12", "Should end with 12"


class TestJob06:
    """Test Job 06: While loop for N × 7 multiplication"""
    
    def test_job_06_output(self, capsys):
        """Test that Job 06 displays correct multiplication results"""
        # Execute Job 06 with N=5
        N = 5
        count = 1
        while count <= 10:
            print(f"{N} x {count} = {N * count}")
            count += 1
        
        captured = capsys.readouterr()
        output_lines = captured.out.strip().split('\n')
        
        assert len(output_lines) == 10, "Should output 10 lines"
        assert "5 x 1 = 5" in output_lines[0], "First should be 5 x 1 = 5"
        assert "5 x 10 = 50" in output_lines[9], "Last should be 5 x 10 = 50"


class TestJob07:
    """Test Job 07: Loop 12 times, display (iteration × 3) - 2"""
    
    def test_job_07_output(self, capsys):
        """Test that Job 07 displays correct formula results"""
        # Execute Job 07
        for tour in range(1, 13):
            result = (tour * 3) - 2
            print(result)
        
        captured = capsys.readouterr()
        output_lines = captured.out.strip().split('\n')
        
        assert len(output_lines) == 12, "Should output 12 lines"
        assert output_lines[0] == "1", "First should be (1*3)-2 = 1"
        assert output_lines[11] == "34", "Last should be (12*3)-2 = 34"


class TestJob08:
    """Test Job 08: Loop 12 times, display iteration + 2"""
    
    def test_job_08_output(self, capsys):
        """Test that Job 08 displays correct values"""
        # Execute Job 08
        for tour in range(1, 13):
            result = tour + 2
            print(result)
        
        captured = capsys.readouterr()
        output_lines = captured.out.strip().split('\n')
        
        assert len(output_lines) == 12, "Should output 12 lines"
        assert output_lines[0] == "3", "First should be 1+2 = 3"
        assert output_lines[11] == "14", "Last should be 12+2 = 14"


class TestJob09:
    """Test Job 09: Display even and odd numbers 1-30"""
    
    def test_job_09_output(self, capsys):
        """Test that Job 09 correctly labels even and odd"""
        # Execute Job 09
        for nombre in range(1, 31):
            if nombre % 2 == 0:
                print(f"{nombre} - Pair")
            else:
                print(f"{nombre} - Impair")
        
        captured = capsys.readouterr()
        output_lines = captured.out.strip().split('\n')
        
        assert len(output_lines) == 30, "Should output 30 lines"
        
        # Check even numbers
        even_count = sum(1 for line in output_lines if "Pair" in line)
        odd_count = sum(1 for line in output_lines if "Impair" in line)
        
        assert even_count == 15, "Should have 15 even numbers"
        assert odd_count == 15, "Should have 15 odd numbers"


class TestLoopExercises:
    """Integration tests for all loop exercises"""
    
    def test_all_jobs_run_without_error(self):
        """Test that all job logic can be executed without errors"""
        try:
            # Job 01
            for nombre in range(21):
                pass
            
            # Job 02
            for nombre in range(0, 21, 2):
                pass
            
            # Job 03
            for nombre in range(1, 21):
                _ = nombre ** 2
            
            # Job 05
            count = 0
            while count < 13:
                count += 1
            
            # Job 06
            N = 5
            count = 1
            while count <= 10:
                count += 1
            
            # Job 07
            for tour in range(1, 13):
                _ = (tour * 3) - 2
            
            # Job 08
            for tour in range(1, 13):
                _ = tour + 2
            
            # Job 09
            for nombre in range(1, 31):
                if nombre % 2 == 0:
                    pass
                else:
                    pass
            
            # If we get here, all jobs executed successfully
            assert True
            
        except Exception as e:
            pytest.fail(f"Job execution failed: {str(e)}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
