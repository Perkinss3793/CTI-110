{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNsEn/i93PLTs7AuMnx8b2h",
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
        "<a href=\"https://colab.research.google.com/github/Perkinss3793/CTI-110/blob/main/P2HW1_PerkinsSkyy.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 83,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z1FEDtnGPxCD",
        "outputId": "eaf438eb-4b02-492e-c5b4-762bfb64c779"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your budget amount: 2000\n",
            "Enter your travel destination: New York City\n",
            "Enter the estimated amount of money that you will spend for gas: 450\n",
            "Enter the approximate amount that you will need for accomodation/hotel: 600\n",
            "Enter the amount that you will spend for food: 250\n",
            "----------------Travel Expenses-------------\n",
            "Location:               New York City\n",
            "Initial Budget:          2,000.00\n",
            "Gas Expense:             450.00\n",
            "Accomodation Expense:    600.00\n",
            "Food Expense:            250.00\n",
            "--------------------------------------------------\n",
            "The remaining balance: 700.0\n"
          ]
        }
      ],
      "source": [
        "# Skyy Perkins\n",
        "# 9/13/2026\n",
        "# Corrected - P1HW2 - 24Sep26\n",
        "#This program will use P1HW2 to proper format string headings that describe columns of data in python.\n",
        "\n",
        "# Get your budget amount\n",
        "budget_amount = float(input(\"Enter your budget amount: \"))\n",
        "\n",
        "# Get your travel destination\n",
        "travel_destination = input(\"Enter your travel destination: \")\n",
        "\n",
        "# Get your gas expense\n",
        "gas_expense = float(input(\"Enter the estimated amount of money that you will spend for gas: \"))\n",
        "\n",
        "# Get your accomodation expense\n",
        "accomodation_expense = float(input(\"Enter the approximate amount that you will need for accomodation/hotel: \"))\n",
        "\n",
        "# Get your food expense\n",
        "food_expense = float(input(\"Enter the amount that you will spend for food: \"))\n",
        "\n",
        "print(\"----------------Travel Expenses-------------\")\n",
        "\n",
        "\n",
        "#Display Travel Destination\n",
        "print(f\"Location:{travel_destination: >28}\")\n",
        "\n",
        "\n",
        "#Display Initial Budget\n",
        "print(f\"Initial Budget: {budget_amount: >17,.2f}\")\n",
        "\n",
        "#Display Fuel Expense\n",
        "print(f\"Gas Expense: {gas_expense: >18,.2f}\")\n",
        "\n",
        "#Display Accomodation Expense\n",
        "print(f\"Accomodation Expense: {accomodation_expense: >9,.2f}\")\n",
        "\n",
        "#Display Food Expense\n",
        "print(f\"Food Expense: {food_expense: >17,.2f}\")\n",
        "\n",
        "#Display hyphen line\n",
        "print(\"-\" * 50)\n",
        "\n",
        "# Add expenses\n",
        "add_expenses = gas_expense + accomodation_expense + food_expense\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "#Display Remaining Balance\n",
        "remaining_balance = budget_amount - gas_expense - accomodation_expense - food_expense\n",
        "print(\"The remaining balance:\" , remaining_balance)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "sJilyi2yget2"
      },
      "execution_count": 83,
      "outputs": []
    }
  ]
}