{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "day2.py",
      "version": "0.3.2",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/xyf0750/python/blob/master/day2_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "39L423NCWzAa",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "a = 5\n",
        "b = 10\n",
        "c = 3\n",
        "d = 4\n",
        "e = 5\n",
        "a += b\n",
        "a -= c\n",
        "a *= d\n",
        "a /= e\n",
        "print(\"a = \", a)\n",
        "\n",
        "flag1 = 3 > 2\n",
        "flag2 = 2 < 1\n",
        "flag3 = flag1 and flag2\n",
        "flag4 = flag1 or flag2\n",
        "flag5 = not flag1\n",
        "print(\"flag1 = \", flag1)\n",
        "print(\"flag2 = \", flag2)\n",
        "print(\"flag3 = \", flag3)\n",
        "print(\"flag4 = \", flag4)\n",
        "print(\"flag5 = \", flag5)\n",
        "print(flag1 is True)\n",
        "print(flag2 is not False)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jpRIwq9eizsQ",
        "colab_type": "code",
        "outputId": "eef67b75-a88d-44f2-a108-08ca7611b3ba",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        }
      },
      "source": [
        "\"\"\"\n",
        "将华氏温度转换为摄氏温度\n",
        "F = 1.8C + 32\n",
        "\n",
        "Version: 0.1\n",
        "Author: 骆昊\n",
        "\"\"\"\n",
        "f = float(input('请输入华氏温度: '))\n",
        "c = (f - 32) / 1.8\n",
        "print('%.1f华氏度 = %.1f摄氏度' % (f,c))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "请输入华氏温度: 111.21\n",
            "111.2华氏度 = 44.0摄氏度\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IlTgXaYhZesN",
        "colab_type": "code",
        "outputId": "7a5d22bc-1a76-4e1a-cd7d-4815fb4dac3a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 69
        }
      },
      "source": [
        "'''\n",
        "输入半径计算圆的周长和面积\n",
        "'''\n",
        "import math\n",
        "radius = float(input('请输入圆的半径: '))\n",
        "perimeter = 2 * math.pi * radius\n",
        "area = math.pi * radius * radius\n",
        "print('周长: %.2f' % perimeter)\n",
        "print('面积: %.2f' % area)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "请输入圆的半径: 10\n",
            "周长: 62.83\n",
            "面积: 314.16\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "W0TqZ-mMaSgi",
        "colab_type": "code",
        "outputId": "e8384c1b-57dd-41e8-df7b-47686d739ed6",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        }
      },
      "source": [
        "\"\"\"\n",
        "输入年份 如果是闰年输出True 否则输出False\n",
        "\n",
        "Version: 0.1\n",
        "Author: 骆昊\n",
        "\"\"\"\n",
        "\n",
        "year = int(input('请输入年份: '))\n",
        "# 如果代码太长写成一行不便于阅读 可以使用\\或()折行\n",
        "is_leap = (year % 4 == 0 and year % 100 != 0 or\n",
        "           year % 400 == 0)\n",
        "print(is_leap)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "请输入年份: 2020\n",
            "True\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}