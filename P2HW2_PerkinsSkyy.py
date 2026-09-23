{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNov6BEEcWgmx73iWfo46gj",
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
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 402
        },
        "id": "L-Bt0KbHzd4W",
        "outputId": "162ae509-1963-4105-a5ad-ee9368f095c4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the grade for Module 1: 100\n",
            "Enter the grade for Module 2: 90\n",
            "Enter the grade for Module 3: 80\n",
            "Enter the grade for Module 4: 70\n",
            "Enter the grade for Module 5: 60\n",
            "Enter the grade for Module 6: 50\n",
            "-----------Results-----------\n",
            "Lowest grade: 50.0\n",
            "Highest grade: 100.0\n",
            "Sum of grades:  450.0\n",
            "Average:\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "'float' object is not iterable",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_2149/3984771325.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     34\u001b[0m \u001b[0;31m# Average of test grades\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     35\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Average:\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 36\u001b[0;31m \u001b[0mAverage\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msum\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msum_total\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m/\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtest_grades\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     37\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     38\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: 'float' object is not iterable"
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
        "print(f\"Lowest Grade: {min (test_grades)}\")\n",
        "\n",
        "# Display the highest grade\n",
        "print(f\"Highest Grade: {max (test_grades)}\")\n",
        "\n",
        "# Add all of test grades to get the sum\n",
        "sum_total = sum(test_grades)\n",
        "\n",
        "# Display the sum of all test grades\n",
        "print(f\"Sum of Grades: {sum_total: .1f}\")\n",
        "\n",
        "# Get the number of items in the list\n",
        "len = (test_grades)\n",
        "\n",
        "# Average of test grades\n",
        "print(\"Average: .2f\")\n",
        "Average = sum(sum_total) / len(test_grades)\n",
        "\n",
        "\n",
        "\n",
        "print(\"--------------------------------------\")"
      ]
    }
  ]
}