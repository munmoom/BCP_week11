{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled48.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMPxocLNDjP3V2AQwCqM3oR",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/BCP_week11/blob/main/1-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "94EEY7F1ixZ6",
        "outputId": "d90cd2d1-9a54-4573-9432-71cc90947f07"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "946859 2\n",
            "Yes\n"
          ]
        }
      ],
      "source": [
        "ring = input().split()\n",
        "num = ring[0]\n",
        "head = ring[1]\n",
        "h_num = int(head+num)\n",
        "num = int(ring[0])\n",
        "\n",
        "N=0\n",
        "M=0\n",
        "\n",
        "for i in range(2,num//2):\n",
        "  res = num%i\n",
        "  if res==0:\n",
        "    N=1\n",
        "\n",
        "for i in range(2,h_num//2):\n",
        "  res = h_num%i\n",
        "  if res==0:\n",
        "    M=1\n",
        "\n",
        "\n",
        "if M+N == 0:\n",
        "  print('Yes')\n",
        "else:\n",
        "  print('No')"
      ]
    }
  ]
}