{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMFf3TGGwiNE/DHtqEj+o4/",
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
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "L-Bt0KbHzd4W",
        "outputId": "2b77b036-4833-4da0-d513-02ffc3cd9940"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax. Perhaps you forgot a comma? (2249708021.py, line 35)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipykernel_895/2249708021.py\"\u001b[0;36m, line \u001b[0;32m35\u001b[0m\n\u001b[0;31m    average = sum_total / len (test grades)\u001b[0m\n\u001b[0m                               ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax. Perhaps you forgot a comma?\n"
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
        "print(f\"Sum of grades: {sum_total: .2f}\")\n",
        "\n",
        "# Get the number of items in the list\n",
        "len = (f\"Total number of items in lists: {len (test_grades)}\")\n",
        "\n",
        "# Average of test grades\n",
        "average = sum_total / len (test grades)\n",
        "print(\"Average: \")\n",
        "\n",
        "\n",
        "print(\"--------------------------------------\")"
      ]
    }
  ]
}