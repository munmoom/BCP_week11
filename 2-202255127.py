{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled49.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyN9DvFSyQ0/d9r45g4sakKb",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/BCP_week11/blob/main/2-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DSV8u17Dobao",
        "outputId": "4f712018-7dc1-4fae-ba1e-f8e7d69f53fc"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0/5/3\n",
            "hasu\n"
          ]
        }
      ],
      "source": [
        "K, D, A = map(int, input().split('/'))\n",
        "\n",
        "if K+A<D or D==0:\n",
        "  print('hasu')\n",
        "else:\n",
        "  print('gosu')"
      ]
    }
  ]
}