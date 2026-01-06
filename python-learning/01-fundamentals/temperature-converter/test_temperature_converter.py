"""
Unit tests for temperature_converter.py

Run tests with: pytest test_temperature_converter.py
or just: pytest
"""

import pytest
from temperature_converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit
)


# Test Celsius to Fahrenheit
def test_celsius_to_fahrenheit_freezing():
    """Test that 0°C equals 32°F (freezing point of water)."""
    assert celsius_to_fahrenheit(0) == 32


def test_celsius_to_fahrenheit_boiling():
    """Test that 100°C equals 212°F (boiling point of water)."""
    assert celsius_to_fahrenheit(100) == 212


def test_celsius_to_fahrenheit_negative():
    """Test that -40°C equals -40°F (special point where scales meet)."""
    assert celsius_to_fahrenheit(-40) == -40


# Test Fahrenheit to Celsius
def test_fahrenheit_to_celsius_freezing():
    """Test that 32°F equals 0°C."""
    assert fahrenheit_to_celsius(32) == 0


def test_fahrenheit_to_celsius_boiling():
    """Test that 212°F equals 100°C."""
    assert fahrenheit_to_celsius(212) == 100


def test_fahrenheit_to_celsius_body_temp():
    """Test that 98.6°F equals approximately 37°C."""
    result = fahrenheit_to_celsius(98.6)
    assert round(result, 1) == 37.0


# Test Celsius to Kelvin
def test_celsius_to_kelvin_absolute_zero():
    """Test that -273.15°C equals 0K (absolute zero)."""
    assert celsius_to_kelvin(-273.15) == 0


def test_celsius_to_kelvin_freezing():
    """Test that 0°C equals 273.15K."""
    assert celsius_to_kelvin(0) == 273.15


def test_celsius_to_kelvin_boiling():
    """Test that 100°C equals 373.15K."""
    assert celsius_to_kelvin(100) == 373.15


# Test Kelvin to Celsius
def test_kelvin_to_celsius_absolute_zero():
    """Test that 0K equals -273.15°C."""
    assert kelvin_to_celsius(0) == -273.15


def test_kelvin_to_celsius_freezing():
    """Test that 273.15K equals 0°C."""
    assert kelvin_to_celsius(273.15) == 0


# Test Fahrenheit to Kelvin
def test_fahrenheit_to_kelvin_freezing():
    """Test that 32°F equals 273.15K."""
    result = fahrenheit_to_kelvin(32)
    assert round(result, 2) == 273.15


def test_fahrenheit_to_kelvin_absolute_zero():
    """Test that -459.67°F equals 0K (absolute zero in Fahrenheit)."""
    result = fahrenheit_to_kelvin(-459.67)
    assert round(result, 2) == 0


# Test Kelvin to Fahrenheit
def test_kelvin_to_fahrenheit_freezing():
    """Test that 273.15K equals 32°F."""
    result = kelvin_to_fahrenheit(273.15)
    assert round(result, 2) == 32


def test_kelvin_to_fahrenheit_absolute_zero():
    """Test that 0K equals -459.67°F."""
    result = kelvin_to_fahrenheit(0)
    assert round(result, 2) == -459.67


# Test with floating point precision
def test_celsius_fahrenheit_round_trip():
    """Test that converting C->F->C returns original value."""
    original = 25.5
    converted = fahrenheit_to_celsius(celsius_to_fahrenheit(original))
    assert round(converted, 10) == original


def test_kelvin_celsius_round_trip():
    """Test that converting K->C->K returns original value."""
    original = 300
    converted = celsius_to_kelvin(kelvin_to_celsius(original))
    assert round(converted, 10) == original