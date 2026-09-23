{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP8P3aXP9VAkbr1HSEd9r3d",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Perkinss3793/CTI-110/blob/main/P2HW2_PerkinsSkyy.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L-Bt0KbHzd4W",
        "outputId": "7f3a6955-37e3-42e1-b01f-3b3fed19530b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the test grade for Module 1: 100\n",
            "Enter the test grade for Module 2: 90\n",
            "Enter the test grade for Module 3: 80\n",
            "Enter the test grade for Module 4: 70\n",
            "Enter the test grade for Module 5: 60\n",
            "Enter the test grade for Module 6: 50\n",
            "-----------Results-----------\n",
            "Your lowest grade is 50.0\n",
            "Your highest grade is 100.0\n",
            "The sum of test grades is  450.00\n",
            "Total number of items in\n",
            "----------------------\n"
          ]
        }
      ],
      "source": [
        "# Skyy Perkins\n",
        "# 09/22/2026\n",
        "# P2HW2\n",
        "# Write a program that asks the user to enter test grades for Modules 1 - 6 and performing computational functions.\n",
        "\n",
        "# Get six test grades for module 1 - module 6 from user\n",
        "Module1 = float(input(\"Enter the test grade for Module 1: \"))\n",
        "Module2 = float(input(\"Enter the test grade for Module 2: \"))\n",
        "Module3 = float(input(\"Enter the test grade for Module 3: \"))\n",
        "Module4 = float(input(\"Enter the test grade for Module 4: \"))\n",
        "Module5 = float(input(\"Enter the test grade for Module 5: \"))\n",
        "Module6 = float(input(\"Enter the test grade for Module 6: \"))\n",
        "\n",
        "# Store grades in a list\n",
        "test_grades = [Module1, Module2, Module3, Module4, Module5, Module6]\n",
        "\n",
        "print(\"-----------Results-----------\")\n",
        "\n",
        "# Display the lowest test grade\n",
        "print(f\"Your lowest grade is {min (test_grades)}\")\n",
        "\n",
        "# Display the highest grade\n",
        "print(f\"Your highest grade is {max (test_grades)}\")\n",
        "\n",
        "# Add all of test grades to get the sum\n",
        "sum_total = sum(test_grades)\n",
        "\n",
        "# Display the sum of all test grades\n",
        "print(f\"The sum of test grades is {sum_total: .2f}\")\n",
        "\n",
        "# Get the number of items in the list\n",
        "print(f\"Total number of items in lists: {}\")\n",
        "\n",
        "# Average of test grades\n",
        "average = sum (test_grades) / len (test_grades)\n",
        "\n",
        "print(\"----------------------\")"
      ]
    }
  ]
}