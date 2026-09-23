{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPcFskSe6IkfTBCR2KX4QKw",
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
      "execution_count": 29,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L-Bt0KbHzd4W",
        "outputId": "e6618e3e-7404-45d3-c8bb-e6611f8db824"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the grade for Module 1: 80\n",
            "Enter the grade for Module 2: 70\n",
            "Enter the grade for Module 3: 60\n",
            "Enter the grade for Module 4: 50\n",
            "Enter the grade for Module 5: 40\n",
            "Enter the grade for Module 6: 30\n",
            "-----------Results-----------\n",
            "Lowest grade: 30.0\n",
            "Highest grade: 80.0\n",
            "Sum of grades:  330.0\n",
            "Average: {(sum_total) / (len)}\n",
            "--------------------------------------\n"
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
        "Module1 = float(input(\"Enter the grade for Module 1: \"))\n",
        "Module2 = float(input(\"Enter the grade for Module 2: \"))\n",
        "Module3 = float(input(\"Enter the grade for Module 3: \"))\n",
        "Module4 = float(input(\"Enter the grade for Module 4: \"))\n",
        "Module5 = float(input(\"Enter the grade for Module 5: \"))\n",
        "Module6 = float(input(\"Enter the grade for Module 6: \"))\n",
        "\n",
        "# Store grades in a list\n",
        "test_grades = [Module1, Module2, Module3, Module4, Module5, Module6]\n",
        "\n",
        "print(\"-----------Results-----------\")\n",
        "\n",
        "# Display the lowest test grade\n",
        "print(f\"Lowest grade: {min (test_grades)}\")\n",
        "\n",
        "# Display the highest grade\n",
        "print(f\"Highest grade: {max (test_grades)}\")\n",
        "\n",
        "# Add all of test grades to get the sum\n",
        "sum_total = sum(test_grades)\n",
        "\n",
        "# Display the sum of all test grades\n",
        "print(f\"Sum of grades: {sum_total: .1f}\")\n",
        "\n",
        "# Get the number of items in the list\n",
        "len = (test_grades)\n",
        "\n",
        "# Average of test grades\n",
        "\n",
        "print(\"Average: {(sum_total) / (len)}\")\n",
        "\n",
        "\n",
        "print(\"--------------------------------------\")"
      ]
    }
  ]
}