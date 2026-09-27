{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMNHHng5M0NWNMYoNq7fgEb",
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
        "<a href=\"https://colab.research.google.com/github/Perkinss3793/CTI-110/blob/main/P1HW2_PerkinsSkyyContinued.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "z1FEDtnGPxCD"
      },
      "outputs": [],
      "source": [
        "# Skyy Perkins\n",
        "# 9/13/2026\n",
        "# Corrected - P1HW2 - 24Sep26\n",
        "#This program calculates and displays travel expenses\n",
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
        "print(\"--------------Travel Expenses-------------\")\n",
        "\n",
        "#Display Travel Destination\n",
        "print(f\"Location: {travel_destination}\")\n",
        "\n",
        "#Display Initial Budget\n",
        "print(f\"Initial Budget: {budget_amount}\")\n",
        "\n",
        "\n",
        "#Display Fuel Expense\n",
        "print(f\"Gas Expense: {gas_expense}\")\n",
        "\n",
        "#Display Accomodation Expense\n",
        "print(f\"Accomodation Expense: {accomodation_expense}\")\n",
        "\n",
        "#Display Food Expense\n",
        "print(f\"Food Expense: {food_expense}\")\n",
        "\n",
        "# Add expenses\n",
        "add_expenses = gas_expense + accomodation_expense + food_expense\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "#Display Remaining Balance\n",
        "remaining_balance = budget_amount - gas_expense - accomodation_expense - food_expense\n",
        "print(\"The remaining balance:\", remaining_balance)"
      ]
    }
  ]
}