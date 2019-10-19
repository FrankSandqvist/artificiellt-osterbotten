html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />
        <meta property="og:image" content="{photo_url}">
        <title>Artificiellt Österbotten - {headline}</title>
        <link
            href="https://fonts.googleapis.com/css?family=Playfair+Display&display=swap"
            rel="stylesheet"
        />
        <link
            href="https://fonts.googleapis.com/css?family=Open+Sans&display=swap"
            rel="stylesheet"
        />
        <link
            href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASQAAAEiCAYAAABQoK/xAAAMS2lDQ1BJQ0MgUHJvZmlsZQAASImVVwdYU8kWnltSSWiBCEgJvYlSpEsJoUUQkCrYCEkgocSQEETsLIsKrl1EQF3RVREXd3UFZK2oa10Eu2t5KKKirIsFGypvUkDX/d573zvfN/f+OXPOf0rm3jsDgE4tTyrNRXUByJMUyOIjQlhTUtNYpG6AAxSQgBcw5PHlUnZcXDSAMnz/u7y+BhDl/bKLkuuf8/9V9ARCOR8AJA7iDIGcnwfxLwDgpXyprAAAog/UW88ukCrxNIgNZDBBiKVKnKXGpUqcocZVKpvEeA7EewAg03g8WRYA2i1QzyrkZ0Ee7RsQu0oEYgkAOmSIA/kingDiSIjH5OXNUmJoBxwyvuDJ+htnxggnj5c1gtW1qIQcKpZLc3lz/s92/G/Jy1UMx7CDgyaSRcYra4Z9u5EzK0qJaRD3STJiYiHWh/itWKCyhxilihSRSWp71JQv58CeASbErgJeaBTEphCHS3JjojX6jExxOBdiuELQInEBN1Hju1QoD0vQcNbKZsXHDuNMGYet8W3kyVRxlfYnFTlJbA3/DZGQO8z/qliUmKLOGaMWipNjINaGmCnPSYhS22A2xSJOzLCNTBGvzN8GYj+hJCJEzY/NyJSFx2vsZXny4XqxpSIxN0aDqwtEiZEanj18nip/I4hbhBJ20jCPUD4lergWgTA0TF071iGUJGnqxbqkBSHxGt8X0tw4jT1OFeZGKPVWEJvKCxM0vnhgAVyQan48RloQl6jOE8/I5k2MU+eDF4FowAGhgAUUcGSAWSAbiNv7mvvgL/VMOOABGcgCQuCi0Qx7pKhmJPCaAIrBnxAJgXzEL0Q1KwSFUP9xRKu+uoBM1WyhyiMHPIQ4D0SBXPhbofKSjERLBg+gRvyP6HyYay4cyrl/6thQE63RKIZ5WTrDlsQwYigxkhhOdMRN8EDcH4+G12A43HEf3Hc428/2hIeETsJ9wlVCF+HmTHGJ7Kt6WGAS6IIRwjU1Z3xZM24HWT3xEDwA8kNunImbABd8PIzExoNgbE+o5WgyV1b/Nfffavii6xo7iisFpYyiBFMcvvbUdtL2HGFR9vTLDqlzzRjpK2dk5uv4nC86LYD3qK8tsaXYfuw0dhw7ix3CmgELO4q1YBeww0o8sooeqFbRcLR4VT45kEf8j3g8TUxlJ+WuDa69rh/UcwXCIuX7EXBmSefIxFmiAhYbvvmFLK6EP3YMy93VzRcA5XdE/Zp6yVR9HxDmuc+6/GMA+JZDZdZnHc8agIMPAWC8/qyzfgEfj1UAHO7gK2SFah2uvBAAFejAJ8oYmANr4ADrcYdfK38QDMLARBALEkEqmAG7LILrWQZmg3lgMSgDFWAVWA+qwRawDewCP4J9oBkcAsfBb+A86ABXwS24enrAU9APXoNBBEFICB1hIMaIBWKLOCPuiA8SiIQh0Ug8koqkI1mIBFEg85BvkApkDVKNbEXqkZ+Rg8hx5CzSidxE7iG9yAvkPYqhNNQANUPt0HGoD8pGo9BEdDqaheajxWgpugKtQuvQPWgTehw9j15Fu9Cn6AAGMC2MiVliLpgPxsFisTQsE5NhC7ByrBKrwxqxVvg/X8a6sD7sHU7EGTgLd4ErOBJPwvl4Pr4AX45X47vwJvwkfhm/h/fjnwh0ginBmeBH4BKmELIIswllhErCDsIBwin4NPUQXhOJRCbRnugNn8ZUYjZxLnE5cRNxL/EYsZPYTRwgkUjGJGdSACmWxCMVkMpIG0l7SEdJl0g9pLdkLbIF2Z0cTk4jS8gl5ErybvIR8iXyI/IgRZdiS/GjxFIElDmUlZTtlFbKRUoPZZCqR7WnBlATqdnUxdQqaiP1FPU29aWWlpaVlq/WZC2x1iKtKq2ftM5o3dN6R9OnOdE4tGk0BW0FbSftGO0m7SWdTrejB9PT6AX0FfR6+gn6XfpbbYb2WG2utkB7oXaNdpP2Je1nOhQdWx22zgydYp1Knf06F3X6dCm6drocXZ7uAt0a3YO613UH9Bh6bnqxenl6y/V2653Ve6xP0rfTD9MX6Jfqb9M/od/NwBjWDA6Dz/iGsZ1xitFjQDSwN+AaZBtUGPxo0G7Qb6hvON4w2bDIsMbwsGEXE2PaMbnMXOZK5j7mNeb7UWaj2KOEo5aNahx1adQbo9FGwUZCo3KjvUZXjd4bs4zDjHOMVxs3G98xwU2cTCabzDbZbHLKpG+0wWj/0fzR5aP3jf7DFDV1Mo03nWu6zfSC6YCZuVmEmdRso9kJsz5zpnmwebb5OvMj5r0WDItAC7HFOoujFk9Yhiw2K5dVxTrJ6rc0tYy0VFhutWy3HLSyt0qyKrHaa3XHmmrtY51pvc66zbrfxsJmks08mwabP2wptj62ItsNtqdt39jZ26XYLbFrtntsb2TPtS+2b7C/7UB3CHLId6hzuOJIdPRxzHHc5NjhhDp5OomcapwuOqPOXs5i503OnWMIY3zHSMbUjbnuQnNhuxS6NLjcG8scGz22ZGzz2GfjbMaljVs97vS4T66errmu211vuem7TXQrcWt1e+Hu5M53r3G/4kH3CPdY6NHi8Xy883jh+M3jb3gyPCd5LvFs8/zo5e0l82r06vW28U73rvW+7mPgE+ez3OeML8E3xHeh7yHfd35efgV++/z+8nfxz/Hf7f94gv0E4YTtE7oDrAJ4AVsDugJZgemB3wd2BVkG8YLqgu4HWwcLgncEP2I7srPZe9jPQlxDZCEHQt5w/DjzOcdCsdCI0PLQ9jD9sKSw6rC74VbhWeEN4f0RnhFzI45FEiKjIldHXueacfncem7/RO+J8yeejKJFJURVR92PdoqWRbdOQidNnLR20u0Y2xhJTHMsiOXGro29E2cflx/362Ti5LjJNZMfxrvFz4s/ncBImJmwO+F1YkjiysRbSQ5JiqS2ZJ3kacn1yW9SQlPWpHRNGTdl/pTzqSap4tSWNFJactqOtIGpYVPXT+2Z5jmtbNq16fbTi6afnWEyI3fG4Zk6M3kz96cT0lPSd6d/4MXy6ngDGdyM2ox+Poe/gf9UECxYJ+gVBgjXCB9lBmSuyXycFZC1NqtXFCSqFPWJOeJq8fPsyOwt2W9yYnN25gzlpuTuzSPnpecdlOhLciQnZ5nPKprVKXWWlkm78v3y1+f3y6JkO+SIfLq8pcAAbtgvKBwU3yruFQYW1hS+nZ08e3+RXpGk6MIcpznL5jwqDi/+YS4+lz+3bZ7lvMXz7s1nz9+6AFmQsaBtofXC0oU9iyIW7VpMXZyz+PcS15I1Ja++SfmmtdSsdFFp97cR3zaUaZfJyq4v8V+yZSm+VLy0fZnHso3LPpULys9VuFZUVnxYzl9+7ju376q+G1qRuaJ9pdfKzauIqySrrq0OWr1rjd6a4jXdayetbVrHWle+7tX6mevPVo6v3LKBukGxoasquqplo83GVRs/VIuqr9aE1OytNa1dVvtmk2DTpc3Bmxu3mG2p2PL+e/H3N7ZGbG2qs6ur3EbcVrjt4fbk7ad/8PmhfofJjoodH3dKdnbtit91st67vn636e6VDWiDoqF3z7Q9HT+G/tjS6NK4dS9zb8VP4CfFT09+Tv/52r6ofW37ffY3/mL7S+0BxoHyJqRpTlN/s6i5qyW1pfPgxINtrf6tB34d++vOQ5aHag4bHl55hHqk9MjQ0eKjA8ekx/qOZx3vbpvZduvElBNXTk4+2X4q6tSZ38J/O3GaffromYAzh876nT14zudc83mv800XPC8c+N3z9wPtXu1NF70vtnT4drR2Tug8cino0vHLoZd/u8K9cv5qzNXOa0nXblyfdr3rhuDG45u5N5//UfjH4K1Ftwm3y+/o3qm8a3q37l+O/9rb5dV1+F7ovQv3E+7f6uZ3P30gf/Chp/Qh/WHlI4tH9Y/dHx/qDe/teDL1Sc9T6dPBvrI/9f6sfebw7Je/gv+60D+lv+e57PnQi+UvjV/ufDX+VdtA3MDd13mvB9+UvzV+u+udz7vT71PePxqc/YH0oeqj48fWT1Gfbg/lDQ1JeTKeaiuAwYFmZgLwYicA9FS4d+gAgDpVfc5TCaI+m6oQ+E9YfRZUiRcAO4MBSFoEQDTco2yGwxZiGrwrt+qJwQD18BgZGpFneriruWjwxEN4OzT00gwAUisAH2VDQ4ObhoY+bofJ3gTgWL76fKkUIjwbfK+tRGfbl5wCX8m/ARlvf4YxlLABAAAACXBIWXMAABYlAAAWJQFJUiTwAAABnWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS40LjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyI+CiAgICAgICAgIDxleGlmOlBpeGVsWERpbWVuc2lvbj4yOTI8L2V4aWY6UGl4ZWxYRGltZW5zaW9uPgogICAgICAgICA8ZXhpZjpQaXhlbFlEaW1lbnNpb24+MjkwPC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+Csu1rd0AAAAcaURPVAAAAAIAAAAAAAAAkQAAACgAAACRAAAAkQAAG2GzfexKAAAbLUlEQVR4AexdCVgV1Rc/7CCoLIIIKCiKqLiBSypYuWaZWpqVS26ZZWVqWlbmmlm5524uaWlpVpqaW5t7LuCuuLCpuIOKAiog/znvH0RPnsybuTNzZ9453/e+N2/m3nPP/d3Ljzsz95xj17d0YD6QEAKEACGgAQJLb1+EPPiXguxW+tXN93dw0cAUapIQIARsHYEWl/YTIdn6JKD+EwK8IECExMtIkB2EACEAREg0CQgBQoAbBIiQuBkKMoQQIASIkGgOEAKEADcIECFxMxRkCCFACBAh0RwgBAgBbhAgQuJmKMgQQoAQIEKiOUAIEALcIECExM1QkCGEACFAhERzgBAgBLhBgAiJm6EgQwgBQoAIieYAIUAIcIMAERI3Q0GGEAKEABESzQFCgBDgBgEiJG6GggwhBAgBIiSaA4QAIcANAkRI3AwFGUIIEAJESDQHCAFCgBsEiJC4GQoyhBAgBIiQaA4QAoQANwgQIXEzFGQIIUAIECHRHCAECAFuECBC4mYoyBBCgBAgQqI5YDMIuAT6Q6mqweDs7wsObq6Qn5MLOek3ITv5AmSePMs1DnZOjuBRsxq4VgoAR88yYOfgAHl3MuHepauQdToJ7l9L59p+scYRIYlFisrpEoEyDeqAb6fW4NOyGbgGB1rsQ15WNtzYtheub/gTrv60yWI5NS84lHIDvy7toFy7J8ArpiGAvb3F5jNPJkDa1h1wbc0WyIxPsFiO9wtESLyPENknCQGvmEYQ9FZP4Q+5kdX1cdVxYe63kLpwpdV1WVSwc3KCSu/0gaDXuwGSkrVybd3vcH7mUrhz7JS1VTUvT4Sk+RCQASwRsHOwh9BPhkFAr86y1d4+eBwSRk2FjNhjsnWJVeDTJgZCxw013ZqJrWOpXMqUhZAy5StLl7k8T4TE5bCQUVIQcAsNhhqzx4FHnXAp1S3WOT30E7j8/TqL11ldqDSoN4SMeIOVOpOe9K074eRboyDvdiZTvUopI0JSClnSqyoC7jWqQsS308Clgp8i7SZ8PBVSFyl3C1d55FtQcWBPRWzHFd6xnkMg92aGIvpZKiVCYokm6dIEAWc/H6i7ZgG4hQQp2v6pQWPgyuqNzNtQYmVkbuTNnQfgSNc3zU9z95sIibshIYOsRSBi2VTwbtXM2mrWl8/Ph9jWPSHzxBnr61qo4dM6BmotnWzhKtvTF5eshrMfTWKrlLE2IiTGgJI6dREI7P8ShI4dolqjLFcauLeo4fZVj9yOwLpjx/sMh7TN21mrZaaPCIkZlKRIbQRwg2DjfWvBwaOUqk2fGjIerqxcL7vNkOGvQaUh/WTrsUYBru5iW/WwpoqqZYmQVIWbGmOJQPC7/SH43VdZqhSlCzcexrboJqqspUIOpd2hyeGNYO/qYqmIYueVehbGwmAiJBYokg5NEHjs4AZwLl9Ok7aPvTIU0n/bJbntwH4vQuj4oZLry6l4a08cHO7MdnuBHHuK1iVCKooGHesGAe8nm0DE8uma2XtZuGU7Ldy6SRV8K1i2UV2p1WXX29+0s8mHT7YixgqIkBgDSurUQaDK6HcgaIC82yY5lt6/ch3+rv+MJBVOXmWhyfEtkuqyqnTm/c/g0jc/s1LHTA8REjMoSZGaCNT75StAx1ktReoqw7tFU9MmTi1tl7vCU8p2IiSlkCW9iiLQNP43cCxTWtE2SlIu9TmS2lsViuvH7bjjcLB93+IuaXqOCElT+KlxKQg4uLtBszN/SanKtM6Z4RPh0vI1Vuus8vEgCHqju9X1WFbAiAZ7o55lqZKJLiIkJjCSEjURcPb1hseEV+ZaS8KY6ZC64Durzaj22ftQ4ZXnra7HskJuxh3YHd6SpUomuoiQmMBIStREwMnHC5oc1T6ImlSH26oThkNAny5qQvZQW+hou7tm64fOa32CCEnrEaD2rUYAXS5iUqTvAbK6QQsVTr0zFq788KuFq5ZPh7w3ACoN1vb5DYbtxYfyvAkREm8jQvaIQqDxgV/AJaC8qLJKFcLNhbjJ0Frx79YRwiZ/aG01puVv7NgHR198m6lOFsqIkFigSDpURyBi6RTwbh2tertFG9xTqw3k3LhV9JSo49KRtaD++sWiyipV6ML8FZA4doZS6iXrJUKSDB1V1BIBDGaGQc20EoxXHdfmFcnN41tCfFuolZzo9z5c3/iXVs1bbJcIySI0dIFnBNxrhELU7ys0M/HctEWQPGmB5PbD54wHv05tJNeXUzE/Nw92hT0JD+7ek6NGkbpESIrASkrVQKDuz/OhbON6ajT1UBsHnnwZsk4lPnRe7Ak1A7OZ28TrLm20kwjJfLTot24Q8HuuLYQLQf3VFszddqL/CNnNRm5ZBh4R1WXrsVbBoWf7qZpJxRr7iJCsQYvKcoeAFj5tB5/pC5giSa74dmgNNeZ9IleNVfWv/rgR4t8eY1UdNQsTIamJNrXFHAHPppFQZ/Vc5notKbwwdzkkjv/S0mWrz9dcMBHKtW9hdT0pFR5k34UDT7wEd89fklJdlTpESKrATI0oiQCGgcVwsEpLxoEjcKhDf6bNYIC5+hu/Bhd/X6Z6i1N2avA4uLJqQ3GXuDlHhMTNUJAhchAIm/Yx+L/YXo6KR9a9d/EKHOkyUJGgZqZV3g9zAOzsHmmDnIspUxdBymTpbwXltG1NXSIka9CislwjUH3GaCj/wtPMbcRbHMzWwTL9kbmR3i2bQq3FX4Cdk5P5Jdm/z89cCkkTBcLTgRAh6WCQyETxCGAqaky8yEow7RFmGbmXepmVSot6StevBdWnjoRS1atYLGPthYSRUyB18Sprq2lWnghJM+ipYaUQQJeSyh8MBPfwUFlN4MZH3ACppuAKqcqotwGTAMiRm7vjIOnTWYCB2PQkREh6Gi2y1SoEAnp3gYBena1aceDuZQy6lvrV93D33EWr2mNZ2KN2dQh89SWrb0Ez9h8GzFB7dY22MbulYkGEJBU5qqcbBHA3t5eQpQRjcLuHVwEnb89C2x/cuw/ZiedM+4pu7NgPaZu2AZ7jRTD2k0+bGPBsFgUedcLBLaQi2Dk6FJqHyQYyT56FW3sPQfrvuwF97PQsREh6Hj2yXRIC9i7OYO/mCvm5uZB3J0uSDi0rOZbxML2Ry8vKhvycXC1NYd42ERJzSEkhIUAISEWACEkqclSPECAEmCNAhMQcUlJICBACUhEgQpKKHNUjBAgB5ggQITGHlBQSAoSAVASIkKQiR/UIAUKAOQJESMwhJYWEACEgFQEiJDPkMIKfT9sYs7P6+5kyZaH+jNahxQ4epcDJqyw4Ch/8Ljz2Lgs56bcgV8hKgplJ8FNwrMe9T2oNDRGSGdJVJwwTsoq+YHZWXz/T/9gNx3oM0ZfRnFqL8YpKVasM7mGVwa1aiOnYRDwC4TgJHyne+fk5OSayQsJCoso6nSh8kiDrTJKwa/w83Lt0lVM0lDeLCMkM4+iEbaZdvGandfUT0yQffLqPIrF7dAWElcZ6NW8EpaqGgFvVYBPxlBK+kZDUlpy0G5B5SiCnhBTITjpvcm259fdByM24o7YpqrdHhFQEcsyEihlRjSDxb42Gqz9tMkJXFO0DhvxAXzGfts1lRwdQ0lD0WUvbskP4bDf5rCnZlpa6iZCKoB/87qsQ/C7bEKVF1Kt6iDFwMBYOycMIuAYHmgjIp01zwGiNepPM+ARI27zdRFAskg3w1H8ipCKj0Xj/WnAJ9C9yRr+HGAfnYPu++u2AApaX79JOIKLHTSsiOydHBVpQXyXGPcJV07W1WwFXUXoXIqR/RtDe1QWiE7frfTz/Yz+rdD3/UarDHxV6dIIKPZ4zhe/QofmiTEYyuvTtz8Jnja6JiQjpn+EO6NMFqk4YLmrw9VJIb+FLWeNqC0RkjpneiYkI6Z8Rjdr8DbjXDjMfX13/xofa+HDb1sQWich8jPVKTERI/4xk84t7zcdU97/xlTHetuE2AFuQ8l2fgcC+XQ19a2btOBYQk142yhIhCSPs21FIaTxX3ZTG1k4sqeVxgyRulDSyOJXzgpD3XheeE3Uycjdl9e3G9n2Q/MU87oP+EyEJw1z7+5mAm+KMKClTvgK9/HeUgr/PU48LZDSA6z1EUvqlRB0MeZv8xXxIXfCdEuqZ6CRCEmA04u1awewwqhuJvbOziYiCBvYo6Cp9i0Tg+vo/TMSUdTZZZA31itk8IXnFNILaK2eqh7jKLaGv1CHhOVJ28gWVW1auOc/oBiYywiwiJNIQwGdLyZ/Pg8vfr5OmQKFaNk9I4XPGg1+nNgrBy4daI7mR+HfrCGGTP+QDWANYkbpwJSSMmspNT2yekJqn/m1KKcPNiChgSOoiYdJ9zM+kk9rFSoP7mlZGUutTveIRQB+5472HFX9R5bM2TUgetcIgcus3KkOufnNGcCPBVRGujkiUQSDzZAIc6tAP8jKzlWlApFabJqTQT9417VsRiZWui+nVjQSTItbf+DW4Va6oa/z1YDySUVzrHpo+b7RpQmoa/xs4limth7ki20Y9upGUiYqAeusWye47KbAOgcPPDTCl5rauFpvSNktILhX8oHEsX28Y2Axp8Vqu/rgR4t8eU/xFDs+WEqIzNti2kkPLbMOkvZHt4d7la6p31mYJKXhoPwge9prqgGvVoMmNRIgimXvrtlYmiG4XV61NjmwEO2cn0XWoIFsEHmTfhd0RbQG/1RSbJaRG+9aCa5AxYh+JnTDHug+G9D/3iC2uWTlcGeEKiURbBDDW0pEub6hqhE0Skr2LM0Qn7VAVaB4a04MbScTSKeDdOpoHuMgGAQGMr3TmvYmqYWGThBTQW4h99KmxYh+JmTHpvwvZSHrym40kdPxQCOz3opiuUBkVETg/exkkTZitSos2SUiRm5eBR+3qqgDMUyM8u5FU6N4Jqk36gCe4yJYiCJwaMh6urFxf5IwyhzZJSEZ2pi1pmsS/OQqu/ry5pGKqXnevWQ3qrJol5DnzVLVdakw8AnfPXzI9T8JvJcXmCMm3gxD7aJ4xYx+JmSg8upFEfDMNvFs2FWM+ldEQAVwh4UpJSbE5Qqr93Zfg9XhjJTHlWjdvbiRGSj3F9cAzMk7pWzebIyRbvl0zzcn8fCE9Uj/gIZ8XropwdUSiHwSUvnWzKULyjG5oelahn+FXxtKzH02Gi0t+UEa5SK12jg5Qf8MSm3y5IBIibotdWbUBTg0ep4h9NkVI4bPHgd9zbRUBUk9KeXAjCez/EoSO5XcLgp7GUwtbcW8S7lFiLTZFSNEJ28DezZU1hrrTZ3IjaSe4kWRo40bi5FUW6m1YDG4hQbrDjgz+PwI512/Aka5vAqb1Zik2Q0j4ajnqt29ZYqdrXVq6kdCDbF1PnULj0zZtg+N93yv8zeLAZgiJdgH/d7po5UbiXL4cRG5aCvhNon8EDnd6DW7tO8ysIzZDSI8d3EB/BEWmjVZuJLQ6KjIIBji8uPRHOPvBF8x6YhOE5OLvC43jlN/2zmxUVFCkhRsJrY5UGFiVm8jNuAOxLbvDvdTLTFq2CUKqNKQfhAy3ndhHYmeG2m4kFV55Hqp99r5Y86icThBIHDsDLsxfwcRamyCkBtuF+DpVQ5gAZiQlaruRYLpyTFtOYiwE8BkSPktiIYYnJMxwGp1se7GPxEyOjNhjcOjZfmKKyi6DMageO/QrOJa1jRjmsgHTmQJWD7cNT0gBvYTYRxO1j32E8Yld8M2SnR0/Uw3dSISstrcPnVDcJu8nm0DE8umKt0MNaIMA3rLhrZtcMTwh1V+/GEpH1pKLk+z6GA7UJcCPu82AarmRVB75FlQc2FM2jrwquH/5Otw+fMKUrSMj9ijkpN+CXCGNeU7aTXDy8QRHYTOok3dZKBNVG8o2rgel69YEZ3/jbH3ADZKxLbrJHh7DExIvzrSXV6wFl6AK4NW8kexBY6lALTcSI8bJzkm/CWmbd0Dalu2Qtmm71cPi81Rz8GkjfNrGGCIW1N6GHWW/bTM0Ifl2aCXEPppg9URRokLSJ7PANTgQKvR8Tgn1knVmJ56Dg5iNRHh9q5TgCwV8sWAkwSB3yZ/Ng7vnLsrulmulAAgZ8bru/SxPvPYBXF//hyw8DE1ItVfMAK8nHpMFEKvKJ14dYbpdw1sX3kRpN5KgAd2gyuh3eOu2JHvy8/IgcfR0SF20SlL9R1UK7NcVqowdDHYODo8qxu21C3O+hcRPZsqyz9CE1PzcHgBHe1kAsaq8v1kXcK9VDWoumMhKJTM9KZMXQMpU5TLE1lk9FzybRjKzVytFeXeyIP6tUabbNKVswNu38FnjwMGjlFJNKKaXRdokwxKSZ3QDIfaROpkSShph9KrfHd4KPOqEm/y4Siqv9nWl3UiM8Pwo51o6nBTikd/csV/x4fGMaQg1hFA5Tr7eirfFsoGsM8lw4HF5WWMMS0jhs8aC3/NPscRbsq4b2/fB0ZfeBmc/H9NeHMmKFKqYK7wRinumD9xNSVWkhSbHtwCGHNGrIC4nB34MGP5XLcE3wzXmjDc9d1SrTbntoDvSnlptZKkxLCHx9Edw7suvhQegc00DxctbP/NZo5QbiZ2DPcScF26ddSr3LlyGoz2HQhbjuD9i4CgVHgq1v5kqvJ3VT4blHRWbQH7eAzHdK7aMIQnJvUZViPp9ebEd1uIkxozB2DEoTY5t5vIVb+rClZAwaipzeNChFiMt6FVOvzsBLq/4RTPz/bt1gLApH2nWvrUN/13/Gbh/5bq11QrLG5KQQscJGVBflXcvW4gQg4O9ke0Bd2qj1BciJZaur/1GTfNuKeVG4lErDCK3fmPenC5+X12zFeLfGKm5reGCD6Bfp9aa2yHGgLjWPeHO8dNiihZbxpCE1GjPT9zce+fezIDdNf+dTJgTDnPDcSfoRiLsR7p9+CRT0zDlFKae0pvgpscjz78BmacSNTfdvXoVqPPTXC5X1ubgHH15ENzYttf8tOjfhiMk3m4R0E8M/9ALpMqoQRD0eveCn1x9K+FGUr5LO6j+5Riu+inGmIRR0yD1q+/FFFWljCkpwjj+kyKcGjQGrqzeKBkTwxFSpcF9IeS9AZIBYV3x6potEC+8oSkQnrNt4ETCCcVSkHyRhPUkWaeTILZVD8jPyeXGbDsnR1NM+FJhlbmxqThDEsd9CRfmSX9+azhCityyDDwiqheHlSbnzk1fDMlfzC9s27d9S6ix4NPC3zwdoBtJXLvekHc7k5lZVUa+DUEDezDTp4aiRMHN58Js/p57Bb3ZE6pwuNO/6JjI3a1tKEKyc3KCmJSdRfHR/Ng89XCZqAiot065XdFyO3y02ztw46+/5aoprF99+igo3/WZwt+8H+RlZsH+pl3g/tU07kzFfWwNd68GB3d+d3HLTSJpKEIK6NVZiH3ENi2L3FlpHriK182RBf1k7UYS8e008G7RtEA999+m6Icd2UQ/VKKzddcugLKN6iqhmonO9D92w7Ee0p91GYqQePSZKm5fRnTSDsAIijwKazeSyM3CLXRtfm6hS8I8dfEPkCCkGudVQicMg8C+L/BqHtw5egri2r4i2T5DERJvu6DzsrJhV9UnHhocnmN84+tufCvIIqwGdrxx7DpwqeD3EAa8njg97FO4vHwtr+aBf/eOEDb5Q27tu3fpKuyNelayfYYhJN9nhYfF8/l6WJx58qwpRYz56GAoVwzpyqvgW0F8O8hC8JkePtvTixzq0B8y9h/h1twyDetAvV++4ta+/Jwc2BEcLdk+wxBSrSWThMh7zSUDoUTFa+t+h5MDHv5vhqmAMCUQr8LKjcTO0QFizu3mtZvF2rW/aWfITrpQ7DUeTrpVDhIebP/IgykWbdgeJPyzfSDNn80whNTszF/C2wc3iyBpccFSuuqKb/aCyh8N1MIkUW2yciOxd3OF6IT/+/CJapiDQrvCWjDd9sC6Sw6l3aHZ6T9Yq2Wqb0dwM8l7uAxBSJ7NoqDOD3OYgspCGa6OcJVkLpibDHOUcSvCf7c44TnSnSPxskx0LOMBTeMf7r8spQpWfnDvPuwMiVGwBTaqMa0Xry9FsIc7K8cAYilFDEFI1WeMhvIvPC2l/4rW2R/9AuBmQ3NB51p0suVZWLiROPl4QZOjm3ju5n9sw3TQext0/M85Hn80PiAkjAjkNyTJztDH4UH2XUnQGYKQGsetBxd/X0kAKFUJg+bvDm9ZrHoMT9rs9J/FXuPlJAs3Et78CkvC1uR32O5fv8OSymt1vf7GJVC6Xk2tmi+x3V1hTwKG+5Uiuick9xqhQuyjFVL6rmidmzv3w5GulgP680iiRQExuZE81UvyxEJdrhUrQKO9a4qq5foYw9M+asx4Mb7Oj3OEGOVRvJjzkB0YrhnDNksR3RNS6NghgA6rvMn52csgacJsi2bVWTULPKMbWrzOwwW5oSTcKleEhrtW89AVUTaYNoXK2GUsqhEGhbgnJCHcDobdkSK6J6QGf30PPHpAn+g/Aq5vsHxbVnXCcAjo00XKmKlWR64bCY4Ljo9eBKN6Hu/Dl+tRcdjxTkh7aj8lZOy9UZzpJZ7TNSHx/IxiX6OOcFeIx2xJAvq8AFUFNwCeJf23XXDslaGSTdRbtMhra7fCyde1jxBZEuC8E9Lf9Z6W7Jysa0Kq9E4fCHn/9ZLGT/Xr+N8B/0s8SvQQSdHkRtKuN9w9f+lRXbF4DR+81v91icXrvF248sOvQjyosbyZ9ZA9vBNS0ZDNDxlfwgldE1K9dQuhTFTtErqo/mUxDqquQiaJRvv49ZkqQO2kEFMaVw5SpEzDulBP8E7Xi1xavgbODJvIvbncE1KDDnDv4hVJOOqWkHiMfVQwApgFFp+/lCSmDW7OziUV0/S6HDcSzFaLERj0IheXrIazH07i3lzeCWlf406SV9W6JST0BUOfMB7leK9hkLZ1R4mm4XYF3LbAs2TEHoVDz74qyUQ93JYW7diF+SsgccyMoqe4POadkEz+gMnS/AF1S0g8e8yLfahXc8FEKNe+BZeTvtAodCMRniNhnBtrxbtVM4hYxj7Xm7V2iC1/buZSSP6UPxckc/u5JyQLHgrm/Sjut24JidewFtbEgwkZ8QZUGtS7uHHh6tzZjyYB3s5YK+XaPQE1F31ubTXNyqdMWSjcavMb2qMAGN4J6UDzFyHrbHKBuVZ965KQcFWBqwsexbSXRchUK0bQ/w798HgXqW4kvh1aQY15E3jvXqF954UVUhKtkArxkHpw4MmXIUtiPjtdEhK3yRaFEUz+fB6cmyHuVTfvAf8LJmR2QgrEoRtJZnbBKVHffp3bQfjMMaLK8lAI87BhPjbehfcVUmzL7oDBCaWIOSH9DwAA///sy0KZAAAYQUlEQVTtnQlcVdX2xxcpmjgmas6iiAPOihNlWqmVvszKynLWNDWH1JzKnpZaDk/NyiHLsXJKmywty1lxBEUBRVQGEXFgUgQFlf9Zt0fv/q/AGfY+5+wNa30+fLjDHtb63suPM+y1ttuGCk2yKhYqCiJb21O/g7vnI0K6eOr1UZC057Am3wqXLgn+p//S1NbuRqd6joSkvUd0uVHxtX9BnQUf6OpjZ+PLa36AiImz7XRB09yNNy+GMv4tNLW1o1FQ576QGhJuaOqnLh+Fe5D1T1830QWpjH9zaLxpyT8Oi/YgwLcT3E2+odktkcXVOYioucsgZsFy55dUH1fq8yL4zJ6k2k6UBvHrt8DZMTNEcSdXP4QXpGf7QerJM7n6n9cb0gmSz5zJUKl397xisu2929GX4Ejbl3TN3/TnZVCqZRNdfexonPjXAQjpO1bX1JUHvAK1Z76rq4+dja/+tB3ODBP/iE50QTredSDcPB5q6KOUTpBaBmyGYl5VDQVrdqdrv/wJp4dO0TVNnflToGLP53X1saNxZmIyHFf+892Ojdc8fdW33oBaU0drbm93w+vbdkPYwIl2u6E6v+iCdOL5N+FG4CnVOHJqIJUgFa/nDS12rs0pDiFeuzD9M4hd8p0uX6q93Rdqvv+2rj52NUaxRdHVajLFhjEl7jwIIb3e0Rqebe1EF6Tg7kMg5UiwIT5SCVKtKSOh6vDehgK1otPJHsMgOSBI11Sez7aHBivm6OpjV+NLX62H81MXaJ6++phB4DV+iOb2djdM3n8MTr4i/j8H4QXppaGQcui4oY9TKkFq/vtqKNG4nqFArei036sd3M/I0DWVR52a4Ld7va4+djXGw3A8HNdqNca9CTXGDdba3PZ2eBfx1GsjbfdDzQESJDVCFrxfpIIntDmx1YKZjE2Reiocgp7pq7uzW6GHoN3Fg7r72dLh/n0Iera/5lu6sglSwvZ9ENpP/IvwwgtSQThlqz6qP3hNGmbL36GWSeNWbYJz783V0vSBNiJfqHd1FmPEWLWYbIJ0/dedEDZ4spbQbG0juiAViIvajTcugjKP+9n6Rchr8jMjp8HVzdvyapLrew3XzIeyHR/L9X2R3rjy/VYIH/2hJpdkE6QryucXPmKaptjsbCS6IOX72/5u7oWhXfQBO78DqnMf9X8Z0qNiVdvl1ACP/PAIUAZLPx+tnJr2g3tp6aruyiZI8et+gbNjZ6rGZXcD0QUpKL8vjBR9xe/99Nuw37u94e9p+W6doP5S8VcIZweIF36T9qmnkVQZ9Bp4T9e3mDJ7Djt+x600ftptpb/CC1KnPpAaetYQEinusvkunw3lnutgKEArOjkuhvY3fjG0mHcNaLlvoxWucpkjas6XEPPpCtWxPGp7gd/eDartRGkQ++VauDBtoSju5OqH6IIU+HQvuHX6XK7+5/WGFILkf2YHFC5VIq84bH0v8uPFcPGL1Uw+PHZuNxTyKMY0hlWd9aSRtD76MxStUtEq15jmiflsFUR9soRpDCs6iy5Ix558HdLCLxhCIbwglev6JPh+NctQcFZ1MrIg0tW3Jj8ug9Ktxc9pQ78zE5Ict//vXIp3DeOB5z5zldzDXmLmHro6Gz1/OUQrScSim/CC9MRrkHYuyhBG4QWprlK+4lGljIXIZmRBpGs8eK0Fr7nIYqeHvq+kkfyl6m65fz0Fvss+UW0nQoOLX6yByJmLRHAlTx9EF6Sjj/WA9MiLecaQ25vCC5Loh/y3L16GI63ZjwAefbUr1P3037l9TsK9rjWNBE+18ZRbBnPE9G/tqTF2xSS8IDHccRZakEq3bQ5NNot9Tn/5258gYgL7EUCxWtWh5f7v7fqO655XTxpJ0y3LoVSLhrrnsLqDY3HrZGOLW630VXRBwn/Q+I/aiAktSN4fKacxb4p9GsOyINL1A2sXEwBuhQu5vizk86x79x3lSLTc3q3x7hCoMXaQkHE4OxW/VlmHNI7WITkzMfL4sF83uBN3xUhXEFqQWuxYC8XrexsKzKpOLAsiXX1s9tsKKNmsgevLwj4/N3kOxK3erOofFqDDQnSiG660P0MrtZk/pkPNukLGleuGxhFWkDzq1gK/XesMBWVlp72VW3ObzmfWRKjUV1/FSW6TGxhITxqJDMsa8CL96bfeN0DC2i6in7IdatoFMq4mGIIirCDJcJiPZToxb4eX4d1EvKsoi2EaSaBS0B1XqquZ79ezoFyXJ9Wa2fp+wh97IbT/eFt90DK56IJ0sNGzjqUhWmJxbSOsIDX5SVmX00rsdTm4WhlXLfMyXECIdxVlspOvjoDk/UdVXRY9/QcDSNp1EE69QRUjVT9MlQZ6N7pwHk5IQSpSviy0Cd7m7KeQj3ksiHQN7Im4w64vCf08evaXEL1QPY0E66BjmRWRLflAIJzsMVxkFx2+iX6EFFDvabh7I9UQRyEFSZbi8DwWRLp+ai3++haK+/q4vizs88Q/90NIv3Ga/Gt5YBMUq1lNU1s7Gt0KjYDAjuKWSM5m4viONBD3O3LApwPcu5We7a6u30IKkgz1gbBULQoSbxN5m6ecYnWkkSjlSLTc5q09czxUHtAjp2GEeA3vDB1q2lUIX/Jyos2J36DIo+XyamLre1j5Qst1xZycFE6QcB3OYxG74aGiRXLyV5jX9BwZ6HFatlIkGNvpt96Da1t2qIbp2bkdNFj1H9V2djXAtVX7qra1a3rN87aLPQhY+lhUYzlzEE6QKr7eDerME//W6/kp8+DSCv4lQ3CLcNzNVia7tGwdnJ/2qarLMqSRBDToDHcTU1RjsatB4bKlwT90u13Ta5p3X3V/yLp7T1Nb10bCCVK9RR9BhRefcfVTuOfHGDKa1YKR7cL2jWMn4US3wWphOd7HVCBMCRLVjrXvCWlnI0V1Dxy71OxZL6x/6NjeKm0AsrIM+SicIOHdNbzLJrrxXBDpGqsMK9SdfcZTHdxx5VZYhPPLOT4WfbOGky/r31svx0BNerGMf3NoLHB+J5Y2PlC7g+HohRIkXDiHC+hEN7yAGz5qmmluej7bQfgcPtfgIybNhstrfnB9+YHnmGSLybai2oUZX0Dsom9EdQ+qvt0Hak0ZIax/t6MvwZG2xrMNhBKk2p9MgMr9XhYWNjmWOwE9aST+YX9C4TKlch/Mxneu/fwn4JbhohrWXi//QidR3QM9VSByCkIoQcLyG1iGg0w+AunnMI2kD9y/fUfV+fpLxP2junXmPAQ++YZqDHY1aLFLSTivJ27CecLveyB04ATDeIQRpNJtmkGTH5YaDoQ62k/g5KtvK2kkx1Qdqajk7NUROGcPF0fiIknRrLiyGBIXRYpsrPXBhBGkmu8Nh2oj+onMmnxTIRA1eynELFyp0gpA9DQSxzKGqerLGFQD5dzA+8N3oMqQ1zmPyne4mAXLIYqhLrkwgtRs60oo2dSXLx0azVICehaLttgp7qlHZlKKI4UkI+6qpfzymqxI5QqOoyP3R0rn1cz29869r2y1ruxvZ9SEECTH2ordYq+tMAq4IPVzpJEo5UjuXFb/Q641dTRgzqKoJtpRkgxHR/hZhg2ZDNd/3Wn4YxVCkPBUDU/ZyOQnoPULWbbT49Bw9TyhAw7pPQYSdwTY7mPZp/2h4bfibz6AoIJffAtSDp8wzEwIQWq04XN4pF0rw0FQR3EIOHZ//VB991cZ0khuHDsFwcpCyayMTNsAuxVxd2x0UcqvkW0+6Jn4aLtXAQv3GTXbBcm9nJK7dWIrwEPiJgsahVsQ++lJI2m0XvlH9ITY/4iilYu00XPsqwdeY4KyQcIY8TdIyP6uB9TrqNRCupn9VPdv2wUJF0Ligkiy/EHAkUairEfSsrd71eG9lVXHI4UP/MzwD+Dqj9YntFZ4sTPUWzxdeD7ZDvIoyWO7IOE22bhdNln+IRAxcRZc/uZH1YBETyNxDiBi/CeAa2ysskq9uwNuQy6T4dbqh1u+wOSyrYKENV3ahmyHwqVLMgVBncUicGXjbxD+zkeanGpzXOxiY85BnJ+6AC4tM/9ucJUhPcH7wzHOU0vx+GbwaTj+XH8mX20VJCwzguVGyPIXgbRzURDUSUkjuZOhGhhuH47biMtikbOWwMWFq0xzt9ro/lBz0jDTxjdz4Ks/bQc8vWUxWwWpzvwpULHn8yz+U19BCZx8ZThg0Xw1Ez2NJCf/49f9AlGzlhreeyynMYtU8ASvSUMBCxTKahc++gxil37H5L6tgtTq8E/wcLVKTAFQZzEJRClHEjGfrVJ1TvQ0ktwCwCJueLSUsG1Pbk00v+75XHvHUREuEJbZeOzCY5sgle34GGAxf7L8SSDhz30Q2u9dTcE1/2MNlGhUV1Nb0RphdQDcYDJB2X3lZmCIZvdKKnWhPJXFoZ7PPCF09r7WgLIyMwHL/95LTdPaJcd2tgmS9zTxEwVzJEYvaiKQeT0JgpTb/3fir6m2x1v/uARAdsPto28cPQmpIeGQmZis7N6aDHeVvLjCSv6Zu2cZcC9bBko0rAulWjYGPEXLT8ZaBymbhW2CJNv+Y9nA6Ld2AvkpjUR71AWzZeQni+Hi56uZg7dFkHCLbNwqmyx/E8ALnHihU80wjQR3WnFzd1drSu8LSoDXphe2CFKNcW9CjXHadqkQlD+5pYGAnjQSTLTFhFsy+Qhc37YbwgZN5OK4LYKElSGxQiRZ/iaAe3M5diM5fU41UFnSSFQDKYANwkd/CFhTnYdZLkgePl7gt2cDD99pDAkIREzQlnIhUxqJBNgtc/H2xctKDfLXAbc/4mGWC1KVwXIui+cBuyCOcWXDrxA+RluCaOvDP0PRahULIiZpY45d/C1cmPE5N/8tF6QGq/+jrL9oxy0AGkhsAo40ko5KGkmGehoJFv7Hldtk8hA43mUA3DwRxs1hSwUJ961vdfhHKORRjFsANJD4BLSu4JUxjUR8+uZ5yPNidraXlgoSfeGysRes31rXqMiaRlKwPs2/o02PioWQN0YD/uZplgpSvc+nQYWXn+PpP40lAYGE7UoaSX9taSS4zTZe4CYTmwDe5scjJN5mnSApJWrbBG6BIo+W4x0DjSc4AUwjCezUGzKuXFf1NL+kkagGKnGD6HlfQfS8r02JwDJBKtflSfD9epYpQdCg4hMIGzwJrv+2S9VRGXYjUQ0iHzfAnDXcWQTXmJlhlglS7ZnjofKAHmbEQGNKQCB2iZJGMl1bGknrY1ugUAkPCaIqeC6G9B0LiX8dMC1wywQJF0PiokiygkngxtFgOPHCEE3B09IQTZgsb3Rp+QY4/4G5JYMsEaQyj7eExhu/sBwgTSgOgb/TSHA3kvOqTlEaiSoiyxvgerLgl4YCXg800ywRJC+lRnD1Uf3NjIPGloCAY+eO79R37qA0EvE+zDMjp8HVzdtMd8wSQaJbuaZ/jlJMEK+kkZzVmEbSMmAz4LokMvsJxCxcCVGzl1riiOmCVLJJfWi2bZUlwfCaJONaIlxes5nXcFzHqdyvB+BuvzJaWsR/dyOhNBJpPj6tNa14BWS6IFUb3gdqThnBy19LxknaewRO9RxpyVx6J2m8cRGUedxPbzdh2ge/PAxSDgap+kOr+lURmd7gyqZtED5qmunzOE9guiA1WrsQHunQxnlO4R9b/V9BDxDv6WOhyqDX9HQRqm3kx0qp0y/US51SGom9HxuPTR+NRGCqIBWrWc1R+8itcCEjvtnWh2fBKd5BOLZYniPXFsvODHCHjtAB451fyvUxXXvMFY2pb9xPvw37vdubOkdug5sqSJX6vAg+syflNrewr+Ouq6mhZ4X0r5RfY2j6y1dC+qbFKT1pJHitrO78DwC3zCKzhgCm9xxqZt9OwqYKUv2lM6F8t47WkOQ0S1r4BTj2dC+A+/c5jch3mEIli4PfzrVQtIq8hczC3lTSSLaqp5Fkk5P9NDU7DtF/66mBblYspgkS7kHlt28juCt7UslkPPYnNzveht8ugLJP+Zs9jWnjG6kySJVGTfs4HANf/eF3ODNiqrmTaBjdNEEq/0InqL9khgYXxGqi9aKrnV7LnhGfciQYgrtrSyNx5owJ2j6zJkq77ME5FpEeW7nOSC1u0wTJZ+5kqNSru9r8wr0f0mcMJO4IEM4vZ4cefaUL1F1o/38zZ5/0PHakkSi72uI21HoN17XV/GAUlPFvrrcrtXchcDflpmPfvPh1v7i8Y99TcwTJzQ1aKSttH65Rxb7IDMx8N/kGBCrXj+5cvmqgt3VdSjSqC83/WGPdhCbMdPbdjyF+7c+GR6a9/Qyjc3TEUjDR879WcgvVt6him0lfb1MECa9v4HUO2Sw5IAiw/rPohju8+u1eB7isQlaLX78Fzo5lO6XHo6TqYwfT0ZKOL0HG1QSIWbAc4laLmYlgiiDVUg6pqw5T7lRJZlaUV+CFxHf5bCj3XAdew1k+TtrZSKWKZB/IysxknpuOlrQhxAvX0QtWQPr5aG0dbGhliiA1374GSjSsa0M4bFOeHTcTRDqfzisar/FDoPqYQXk1Ef49LGeRcug4Fz/paCl3jLdj4yFGOT3Do1LRjbsgybxw73jXgXDzeKjon5nDP1zfheu8ZLbImYvg4iK+18KwKmnlAa+AR20vmdFw8f1eahrErfze8XMn/hqXMc0ehLsgVX9nIHhNeMtsv7mPn34hxnFB+/4d9Q0NuU9uYECPOjXBb9c6AOUGgqyW8PseCB04gbv7WP4WRQl/ilYsz318GQaMW7nJIURYWE0m4y5IjTctkfIi4/Vfd0LYELlyxFrsWAvF63vL9H37f75imZcg3I1EudBqhqEYZQtTQanRfeX7rRC3apM0R/qunztXQfKoW+vv/9qus0jwPGruMsfdBwlc/cfFeounQ4Xunf95LuMDs/b3cmaBp29/C1P+3WQC90jDo6Lk/UedQ5fuMVdBqjLwVfCeMU46COgwZqBjJrpMhmWBsTywzHZx8TcQOcOaeutY0gSXpDzyVFupU2+yP++bQaGQuCtA+TkI+Dg/GFdBarByLng+84R0XPDiX2DHXnA7Jk4q35E1MpfZUg6fcOzzZXUMsopTfhQh58+emyAVrVTBUftIxnN1PVv0OMOz+zH+UbVQMv8ferio3a4Ynj8r8y4EKmkkWGXBLnMWpxKN6kGR8mXtcuWBee/dvAW3ws9D0p7D+epI6IFA//sCN0GSOb8KV62emzwnN0ZCv95s60oo2dRXaB/VnBNt/RfeKCjRoI5yw8AHivvWVn58LBGpzIQkSD0VDqkh4YoIRTpE+pYi1DwWj6p9BqK8z02QRAmI/CACZhB4uGpFKK6IVImGdQBL6xRWyupgaR38yX6c19kBXhbITEqBu8oP/v7ncWKyQ4RuhUUALmAs6EaCVNC/ARQ/NwKYY+heVhEp/FGEyiE8iYr4KD8F6SiHBSgJEgs96ksEiABXAiRIXHHSYESACLAQIEFioUd9iQAR4EqABIkrThqMCBABFgIkSCz0qC8RIAJcCZAgccVJgxEBIsBCgASJhR71JQJEgCsBEiSuOGkwIkAEWAiQILHQo75EgAhwJUCCxBUnDUYEiAALARIkFnrUlwgQAa4ESJC44qTBiAARYCFAgsRCj/oSASLAlQAJElecNBgRIAIsBEiQWOhRXyJABLgSIEHiipMGIwJEgIUACRILPepLBIgAVwIkSFxx0mBEgAiwECBBYqFHfYkAEeBKgASJK04ajAgQARYCJEgs9KgvESACXAmQIHHFSYMRASLAQoAEiYUe9SUCRIArARIkrjhpMCJABFgIkCCx0KO+RIAIcCVAgsQVJw1GBIgACwESJBZ61JcIEAGuBEiQuOKkwYgAEWAhQILEQo/6EgEiwJUACRJXnDQYESACLARIkFjoUV8iQAS4EiBB4oqTBiMCRICFAAkSCz3qSwSIAFcCJEhccdJgRIAIsBAgQWKhR32JABHgSoAEiStOGowIEAEWAiRILPSoLxEgAlwJkCBxxUmDEQEiwEKABImFHvUlAkSAKwESJK44aTAiQARYCJAgsdCjvkSACHAlQILEFScNRgSIAAsBEiQWetSXCBABrgRIkLjipMGIABFgIUCCxEKP+hIBIsCVAAkSV5w0GBEgAiwESJBY6FFfIkAEuBIgQeKKkwYjAkSAhQAJEgs96ksEiABXAiRIXHHSYESACLAQIEFioUd9iQAR4EqABIkrThqMCBABFgIkSCz0qC8RIAJcCZAgccVJgxEBIsBCgASJhR71JQJEgCuBBwSpi0f5LK4z0GBEgAgQAY0E/ki7DvfgfxLkpvT73zONg1AzIkAEiIAZBP4PWC8hSxMgQgsAAAAASUVORK5CYII="
            rel="icon"
            type="image/x-icon"
        />
        <style>
            html,
            body {{
                margin: 0;
                font-family: "Open Sans", sans-serif;
            }}

            .container {{
                width: 100%;
                flex-direction: column;
            }}

            .logocontainer {{
                display: flex;
                max-width: 17rem;
            }}

            .logo {{
                width: 100%;
            }}

            .spacer {{
                flex: 1;
                min-width: 1rem;
            }}

            .header {{
                height: 3rem;
                background-color: black;
                display: flex;
                padding: 1rem;
                align-items: center;
            }}

            .credit {{
                display: inline-block;
                background-color: rgba(0, 0, 0, 0.3);
                color: rgba(255, 255, 255, 0.7);
                font-size: 0.5rem;
                border-radius: 0.2rem;
                padding: 0.2rem;
                margin: 0.5rem;
            }}

            .credit a {{
                color: white;
                text-decoration: none;
            }}

            .image {{
                background-size: cover;
                background-position: center;
                height: 60vw;
                max-height: 60vh;
            }}

            .text {{
                padding: 1rem;
            }}

            h1 {{
                font-family: "Playfair Display", "Arial Black", Arial, Helvetica,
                Verdana, sans-serif;
                font-size: 7vw;
                line-height: 105%;
                padding: 0;
                font-weight: bold;
                letter-spacing: 0;
                margin: 5px 0 12px;
                color: #222;
                margin-bottom: 2rem;
            }}

            @media (min-width: 768px) {{
                h1 {{
                    font-size: 3rem;
                }}
            }}

            .info {{
                color: gray;
            }}

            .info a {{
                color: gray;
                font-weight: 900;
                text-decoration: underline;
            }}

            .home a {{
                color: gray;
                font-size: 0.8rem;
            }}
        </style>
    </head>
    <body>
        <div id="fb-root"></div>
        <script
            async
            defer
            crossorigin="anonymous"
            src="https://connect.facebook.net/sv_SE/sdk.js#xfbml=1&version=v4.0"
        >
        </script>
        <div class="container">
            <div class="header">
                <div class="logocontainer">
                <a href=".">
                    <img
                        alt=""
                        class="logo"
                        src="data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgNjAwMCAxMDAwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2UtbWl0ZXJsaW1pdD0iMS40MSI+CiAgPHBhdGggZmlsbD0iI2MzMTQzMiIgZD0iTTAgMGgxMDAwdjEwMDBIMHoiLz4KICA8cGF0aCBkPSJNNTQ3LjAzIDgwMC41MkgzNzUuNDZsLTE0LjU0LTcxLjE5aC0xMzEuOGwtMTUuOTUgNzEuMTlINTAuMDVsMTc0LjAxLTU2MC44aDE2OS41OGwxNTMuNCA1NjAuOHpNMzM3Ljk0IDYwOS4xbC0xMi42Ni02NS4zOWMtLjMtLjIzLS45NC0zLjUtMS44OC05LjgtLjYyLTUuMzMtMy45LTI2LjQtOS44NC02My4yYTczMy4xIDczMy4xIDAgMCAxLTIuMzUtMTYuODggMjIxMi4yIDIyMTIuMiAwIDAgMC0zLjc2LTI3LjA3bC02LjEtNTMuMDNhMzU4LjgyIDM1OC44MiAwIDAgMS0yLjU3IDE3LjA4Yy0xLjEgNi4yOS0yLjI2IDEzLjItMy41MyAyMC43YTIwOTEuNjcgMjA5MS42NyAwIDAgMS00LjY5IDMxLjIzIDE3Mi4xIDE3Mi4xIDAgMCAxLTEuODYgMTAuNTRsLTEzLjYgNjcuOTItMTkuNzIgODcuOWg4Mi41NnpNNTEyLjEgNTQxLjJjLS4wNS02LS4wNy0xMi4yMy0uMDctMTguNjYgMC02NC42MyAyLjEtMTA3Ljg4IDYuMy0xMjkuNzcgNC40Ny0yMS44OCAxMS4zMy0zOS41NyAyMC41Ni01My4wNSAxNC44My0yNS43IDM4LjYyLTQ4LjYgNzEuMzUtNjguNyAzMi4xOC0yMC4zNiA3Mi4zNC0zMC44IDEyMC40Ny0zMS4zIDQ4LjY4LjUgODkuMjYgMTAuOTQgMTIxLjcyIDMxLjMgMzIuMTggMjAuMSA1NS40IDQzIDY5LjY3IDY4LjcgMTAuMzUgMTMuNDggMTcuNDkgMzEuMTcgMjEuNCA1My4wNSAzLjY1IDIxLjg5IDUuNDYgNjUuMTQgNS40NiAxMjkuNzcgMCA2My42Mi0xLjgxIDEwNi42Mi01LjQ1IDEyOS4wMS0zLjkyIDIyLjQtMTEuMDYgNDAuMzMtMjEuNCA1My44Mi0xNC4yOCAyNS43LTM3LjUgNDguMzUtNjkuNjggNjcuOTQtMzIuNDYgMjAuMzUtNzMuMDQgMzEuMDQtMTIxLjcyIDMyLjA2LTQ4LjEzLTEuMDItODguMjktMTEuNy0xMjAuNDctMzIuMDYtMTYuOTYtMTAuMTUtMzEuNTEtMjEuMTItNDMuNjYtMzIuOWwtNTQuNDktMTk5LjJ6IiBmaWxsPSIjZmZmIiBmaWxsLXJ1bGU9Im5vbnplcm8iLz4KICA8cGF0aCBkPSJNNjY1LjM5IDUyMi4zNmMtLjI2LTguMS0uMzgtMTcuNzQtLjM4LTI4Ljk0IDAtMjYuNjQuNy00NC40NyAyLjA4LTUzLjUgMS40OS05LjAxIDMuNzYtMTYuMyA2LjgzLTIxLjg2IDQuOTItMTAuNiAxMi44MS0yMC4wMyAyMy42Ny0yOC4zMiAxMC42OC04LjQgMjQtMTIuNyAzOS45Ny0xMi45IDE2LjE2LjIgMjkuNjIgNC41IDQwLjQgMTIuOSAxMC42NyA4LjI5IDE4LjM4IDE3LjcyIDIzLjExIDI4LjMyIDMuNDQgNS41NiA1LjggMTIuODUgNy4xIDIxLjg3IDEuMjEgOS4wMiAxLjgxIDI2Ljg1IDEuODEgNTMuNDkgMCAxMS4yLS4xIDIwLjg0LS4zMyAyOC45NC4yMiA4LjE3LjMzIDE3Ljk0LjMzIDI5LjMyIDAgMjYuMjItLjYgNDMuOTQtMS44IDUzLjE3LTEuMyA5LjIzLTMuNjcgMTYuNjMtNy4xIDIyLjE4LTQuNzQgMTAuNi0xMi40NSAxOS45My0yMy4xMyAyOC0xMC43NyA4LjQtMjQuMjMgMTIuOC00MC4zOSAxMy4yMi0xNS45Ni0uNDItMjkuMjktNC44Mi0zOS45Ny0xMy4yMS0xMC44Ni04LjA4LTE4Ljc1LTE3LjQxLTIzLjY3LTI4YTI3My4yMSAyNzMuMjEgMCAwIDEtNC4wNC05LjkyIDcxLjQ0IDcxLjQ0IDAgMCAxLTIuNzktMTIuMjdjLTEuMzktOS4yMy0yLjA4LTI2Ljk1LTIuMDgtNTMuMTcgMC0xMS4zOC4xMi0yMS4xNS4zOC0yOS4zMnoiIGZpbGw9IiNjMzE0MzIiIGZpbGwtcnVsZT0ibm9uemVybyIvPgogIDxjaXJjbGUgY3g9IjQ2OC41IiBjeT0iMTgyLjUiIHI9IjUxLjUiIGZpbGw9IiNmZmYiIHRyYW5zZm9ybT0ibWF0cml4KDEuMTMwOSAwIDAgMS4xNjI5OSAxMTguMTggLTYxLjczKSIvPgogIDxjaXJjbGUgY3g9IjQ2OC41IiBjeT0iMTgyLjUiIHI9IjUxLjUiIGZpbGw9IiNmZmYiIHRyYW5zZm9ybT0ibWF0cml4KDEuMTMwOSAwIDAgMS4xNjI5OSAyODMuMTUgLTYxLjczKSIvPgogIDxnIGZpbGw9IiNmZmYiIGZpbGwtcnVsZT0ibm9uemVybyI+CiAgICA8cGF0aCBkPSJNMTIxOC42OCAyODMuNzVoNTEuOGwxMDUuODUgNDkzLjc1aC02NS44N2wtMTguNTUtOTYuMjVoLTk3Ljg2bC0xOC44NiA5Ni4yNWgtNjMuOTZsMTA3LjQ1LTQ5My43NXptNjMuNjQgMzQ2bC0xNC43LTc4LjY2Yy05LjgyLTUzLjUtMTcuOC0xMTAuNjQtMjMuOTktMTcxLjRhMTcyMC41NyAxNzIwLjU3IDAgMCAxLTExLjUxIDkwLjAyIDMwNjguOTIgMzA2OC45MiAwIDAgMS0xNi42NCA5Ni43M2wtMTIuMTUgNjMuMzJoNzl6TTEzODkuMTUgMjgzLjc1aDg3LjYyYzM2LjI0IDAgNjMuMjEgOC42MyA4MC45IDI1LjkxIDIyLjQgMjIuMzggMzMuNiA1Ni42IDMzLjYgMTAyLjY1IDAgMzUuNC01LjkzIDYzLjc5LTE3Ljc2IDg1LjIyLTExLjg0IDIxLjQzLTI4Ljc0IDM0LjctNTAuNjkgMzkuODJsOTAuODMgMjQwLjE1aC02Ny40OWwtOTAuNS0yNDEuNzVWNzc3LjVoLTY2LjVWMjgzLjc1em02Ni41MiAyMTguNzNjMjUuNzkgMCA0NC4wMi01Ljk2IDU0LjY4LTE3LjkgMTAuNjYtMTEuOTQgMTUuOTgtMzIuMDggMTUuOTgtNjAuNDQgMC0xNS4zNS0xLjExLTI4LjQ2LTMuMzUtMzkuMzQtMi4yNC0xMC44Ny01Ljc1LTE5LjctMTAuNTYtMjYuNTNhNDIuNDcgNDIuNDcgMCAwIDAtMTguNTUtMTUuMDRjLTcuNTUtMy4yLTE2LjU2LTQuOC0yNy4wMi00LjhoLTExLjE4djE2NC4wNXpNMTYwNiAyODMuNzVoMjE2LjQ4djU4LjIxaC03NC41MVY3NzcuNWgtNjUuMjNWMzQxLjk2SDE2MDZ2LTU4LjJ6TTE4MzMuMSAyODMuODJoNjYuNTN2NDkzLjhoLTY2LjU0ek0xOTQ5LjQ5IDI4My43NWgxNzcuOHY1Ni4yOGgtMTExLjNWNDk2LjFoMTAwLjQydjU2LjI4SDIwMTZWNzc3LjVoLTY2LjUxVjI4My43NXpNMjE1Mi4zIDI4My44Mmg2Ni41NHY0OTMuOGgtNjYuNTR6TTI0NjIuNDcgMjkxLjc1djU5LjhjLTE3LjA2LTguMzItMzEuMzMtMTIuNDctNDIuODUtMTIuNDctMTUuNzggMC0yOS4zMSAzLjg5LTQwLjYxIDExLjY3LTExLjMgNy43OC0yMC42MyAxOS43OC0yNy45OCAzNS45OC03LjM2IDE2LjItMTIuOCAzNi43MS0xNi4zMSA2MS41NS0zLjUyIDI0LjgzLTUuMjggNTQuMi01LjI4IDg4LjEgMCAxMjEuOTQgMzEuMjMgMTgyLjkyIDkzLjcgMTgyLjkyIDEwLjg3IDAgMjMuOTgtMy40IDM5LjMzLTEwLjIzdjYxLjA3Yy0xNS45OCA4Ljk2LTMzLjkgMTMuNDMtNTMuNzIgMTMuNDMtMTAwIDAtMTQ5Ljk5LTgxLjY0LTE0OS45OS0yNDQuOTUgMC04OC4yNiAxMi4yMS0xNTMuOTIgMzYuNjMtMTk2Ljk5IDI0LjQtNDMuMDYgNjEuNzctNjQuNTggMTEyLjA4LTY0LjU4IDE4LjU1IDAgMzYuODggNC45IDU1IDE0Ljd6TTI0OTIuMiAyODMuODJoNjYuNTR2NDkzLjhoLTY2LjU0ek0yNjA4LjY2IDI4My43NWgxNzYuODR2NTYuMjhoLTExMC4zM3YxNTYuMzloOTcuODZ2NTYuMjdoLTk3Ljg2djE2OC41M2gxMTAuMzN2NTYuMjhoLTE3Ni44NFYyODMuNzV6TTI4MjAuMzggMjgzLjc1aDY2LjUzdjQzNy40N2gxMDguNzF2NTYuMjhoLTE3NS4yNFYyODMuNzV6TTMwMTEgMjgzLjc1aDY2LjUxdjQzNy40N2gxMDguNzN2NTYuMjhIMzAxMVYyODMuNzV6TTMxNTEuMDggMjgzLjc1aDIxNi41djU4LjIxaC03NC41MVY3NzcuNWgtNjUuMjNWMzQxLjk2aC03Ni43NnYtNTguMnpNMzczNC43NCA1NDIuNzhjMCA4Ny4yLTkuNyAxNDkuMTMtMjkuMSAxODUuNzktMTkuNCAzNi42Ny01MS45IDU1LTk3LjUzIDU1LTQ3Ljk3IDAtODEuNzYtMTkuNzEtMTAxLjM3LTU5LjE1LTE5LjQtMzguNTktMjkuMS0xMDcuMTMtMjkuMS0yMDUuNjIgMC04Ny44NCA5LjYtMTQ5Ljk5IDI4Ljc4LTE4Ni40NCAxOS40LTM2LjY2IDUyLjIzLTU1IDk4LjUtNTUgNDEuMzUgMCA3Mi4wNSAxNC4xNyA5Mi4wOSA0Mi41MyAxMy4yMSAxOC45OCAyMi44MiA0NS45NSAyOC43OCA4MC45IDUuOTcgMzIuNDEgOC45NSA3OS43NCA4Ljk1IDE0MnptLTY5LjcgNy4wNGMwLTg1LjUtMy44NC0xNDIuMi0xMS41Mi0xNzAuMTQtNy42Ny0yOC4xMy0yMy4zNC00Mi4yLTQ3LTQyLjItMjMuNjggMC0zOS40NSAxMi45LTQ3LjMzIDM4LjctNy42OCAyNi0xMS41MSA3OC4yMy0xMS41MSAxNTYuNjkgMCA3Mi4yNiA0LjA0IDEyMi4zNiAxMi4xNSAxNTAuMjkgOC4zIDI2LjQ0IDIzLjg3IDM5LjY2IDQ2LjY4IDM5LjY2IDIyLjM5IDAgMzcuNzQtMTIuMzcgNDYuMDYtMzcuMSA4LjMtMjQuNTEgMTIuNDctNjkuODIgMTIuNDctMTM1Ljl6bS0xMTguOTYtMzg4Ljg3YzkuOCAwIDE4LjIyIDMuNjMgMjUuMjUgMTAuODggNy4wNSA3LjAzIDEwLjU2IDE1LjU2IDEwLjU2IDI1LjU4IDAgMTAuMDItMy42MyAxOC42Ni0xMC44NyAyNS45LTcuMDQgNy4wNC0xNS41NiAxMC41Ni0yNS41OCAxMC41Ni0xMC4wMiAwLTE4LjY2LTMuNTItMjUuOTEtMTAuNTUtNy4wNC03LjI1LTEwLjU1LTE2LTEwLjU1LTI2LjIzIDAtMTAuMDIgMy42Mi0xOC41NCAxMC44Ny0yNS41OCA3LjI1LTcuMDMgMTUuOTgtMTAuNTYgMjYuMjMtMTAuNTZ6bTEyMi40NyAwYzkuOCAwIDE4LjIzIDMuNjMgMjUuMjYgMTAuODggNy4wNCA3LjAzIDEwLjU2IDE1LjU2IDEwLjU2IDI1LjU4IDAgMTAuMDItMy42MyAxOC42Ni0xMC44NyAyNS45LTcuMDQgNy4wNC0xNS41OCAxMC41Ni0yNS42IDEwLjU2LTEwIDAtMTguNjUtMy41Mi0yNS45LTEwLjU1LTcuMDItNy4yNS0xMC41NS0xNi0xMC41NS0yNi4yMyAwLTEwLjAyIDMuNjMtMTguNTQgMTAuODctMjUuNTggNy4yNi03LjAzIDE2LTEwLjU2IDI2LjIzLTEwLjU2ek0zOTM5LjEyIDI5NHY2NC45Yy0yMC4yNy0xNC40OS0zOC40OS0yMS43NS01NC42OS0yMS43NS0xNy40OCAwLTMxLjc2IDYuMTktNDIuODYgMTguNTUtMTEuMDggMTEuNzQtMTYuNjIgMjcuNC0xNi42MiA0Ny4wMSAwIDE3LjI4IDMuOTUgMzIuMSAxMS44MyA0NC40NiA0LjA1IDYuNiAxMC43MiAxNS4xMiAxOS45OSAyNS41OCA5LjI3IDEwLjQ0IDIxLjI2IDIzLjAyIDM1Ljk4IDM3LjczIDI3LjA3IDI3LjUgNDUuNSA1MS4yNyA1NS4zMSA3MS4zMSA5LjgxIDE5LjQgMTQuNzEgNDMuMTcgMTQuNzEgNzEuMyAwIDM4LjE4LTEwLjc2IDY5LjYyLTMyLjMgOTQuMzUtMjEuNTIgMjQuMS00OS4xMyAzNi4xMy04Mi44MiAzNi4xMy0yOC4zNiAwLTUyLjU1LTcuNzgtNzIuNTktMjMuMzR2LTY1Ljg3YzIzLjY3IDE3LjI2IDQ1LjIgMjUuOSA2NC42IDI1LjkgMTguMTIgMCAzMi4zLTYuMDIgNDIuNTMtMTguMDcgMTAuMjMtMTIuMDUgMTUuMzUtMjguNDEgMTUuMzUtNDkuMSAwLTE3LjktMy45NC0zNC0xMS44NC00OC4yNy00LjA0LTYuODMtOS42OS0xNC42Ni0xNi45NS0yMy41LTcuMjQtOC44Ni0xNi4zLTE4LjcyLTI3LjE4LTI5LjU5LTE2Ljg0LTE2LjYyLTMwLjgtMzEuMzMtNDEuODgtNDQuMTMtMTEuMDgtMTIuNzgtMTkuMy0yMy45OC0yNC42My0zMy41Ny0xMC4yMy0xOC43Ny0xNS4zNS00Mi40Mi0xNS4zNS03MSAwLTM4LjU4IDEwLjAyLTY5LjE4IDMwLjA2LTkxLjc3IDIwLjI1LTIyLjgyIDQ3LjQ0LTM0LjIxIDgxLjU1LTM0LjIxIDIzLjY2IDAgNDYuMjYgNS42NCA2Ny44IDE2Ljk0ek0zOTYxLjIgMjgzLjc1aDIxNi40OXY1OC4yMWgtNzQuNVY3NzcuNWgtNjUuMjVWMzQxLjk2aC03Ni43NHYtNTguMnpNNDE4OC4yNyAyODMuNzVoMTc2Ljg0djU2LjI4SDQyNTQuOHYxNTYuMzloOTcuODV2NTYuMjdoLTk3Ljg1djE2OC41M2gxMTAuMzJ2NTYuMjhoLTE3Ni44NFYyODMuNzV6TTQ0MDAgMjgzLjc1aDg3LjYyYzM2LjIzIDAgNjMuMiA4LjYzIDgwLjkgMjUuOTEgMjIuMzggMjIuMzggMzMuNTggNTYuNiAzMy41OCAxMDIuNjUgMCAzNS40LTUuOTIgNjMuNzktMTcuNzUgODUuMjItMTEuODQgMjEuNDMtMjguNzIgMzQuNy01MC42OSAzOS44Mmw5MC44MyAyNDAuMTVINDU1N2wtOTAuNS0yNDEuNzVWNzc3LjVINDQwMFYyODMuNzV6bTY2LjUgMjE4LjczYzI1LjgxIDAgNDQuMDMtNS45NiA1NC43LTE3LjkgMTAuNjYtMTEuOTQgMTUuOTktMzIuMDggMTUuOTktNjAuNDQgMC0xNS4zNS0xLjEzLTI4LjQ2LTMuMzctMzkuMzQtMi4yNC0xMC44Ny01Ljc1LTE5LjctMTAuNTQtMjYuNTNhNDIuNDcgNDIuNDcgMCAwIDAtMTguNTUtMTUuMDRjLTcuNTctMy4yLTE2LjU4LTQuOC0yNy4wMi00LjhoLTExLjJ2MTY0LjA1ek00NjQ5Ljc3IDI4My43NWg5MC4xOGM3MC41NyAwIDEwNS44NSA0My44MiAxMDUuODUgMTMxLjQzIDAgMzMuNDgtNC41OSA1OC4zMS0xMy43NiA3NC41Mi05LjE1IDE2LjItMjUuMzYgMjguNDYtNDguNiAzNi43OCAyNi42NSAxMC42NCA0NC44OCAyNC4zIDU0LjY4IDQwLjkzIDEwLjAyIDE2LjQxIDE1LjA0IDQxLjE0IDE1LjA0IDc0LjE5IDAgOTAuNi0zOC44IDEzNS45LTExNi40IDEzNS45aC04N1YyODMuNzV6bTYyLjY4IDIxNy40NmMyNS44IDAgNDMuNy01Ljk3IDUzLjcyLTE3LjkgMTAuMDItMTIuNiAxNS4wNC0zNC42NSAxNS4wNC02Ni4yIDAtNTMuMy0xOS4yLTc5Ljk2LTU3LjU3LTc5Ljk2aC03Ljk5Yy0xLjcgMC0yLjc4LjEyLTMuMi4zM3YxNjMuNzN6bTAgMjE5LjM3YzI3LjI5IDAgNDYuMTUtNS44NyA1Ni42LTE3LjYgMTAuNDQtMTEuNzEgMTUuNjctMzIuOTMgMTUuNjctNjMuNjIgMC0zMS41Ni01LjQ0LTUzLjYzLTE2LjMxLTY2LjItMTAuNjYtMTIuOC0yOS4zMS0xOS4yLTU1Ljk2LTE5LjJ2MTY2LjYyek01MTM4LjQyIDU0Mi43OGMwIDg3LjItOS42OSAxNDkuMTMtMjkuMSAxODUuNzktMTkuNCAzNi42Ny01MS45IDU1LTk3LjUzIDU1LTQ3Ljk3IDAtODEuNzYtMTkuNzEtMTAxLjM3LTU5LjE1LTE5LjQtMzguNTktMjkuMS0xMDcuMTMtMjkuMS0yMDUuNjIgMC04Ny44NCA5LjYtMTQ5Ljk5IDI4Ljc3LTE4Ni40NCAxOS40Mi0zNi42NiA1Mi4yNC01NSA5OC41LTU1IDQxLjM3IDAgNzIuMDYgMTQuMTcgOTIuMSA0Mi41MyAxMy4yMSAxOC45OCAyMi44MiA0NS45NSAyOC43OCA4MC45IDUuOTcgMzIuNDEgOC45NSA3OS43NCA4Ljk1IDE0MnptLTY5LjcgNy4wNGMwLTg1LjUtMy44NC0xNDIuMi0xMS41Mi0xNzAuMTQtNy42Ny0yOC4xMy0yMy4zNC00Mi4yLTQ3LTQyLjItMjMuNjggMC0zOS40NSAxMi45LTQ3LjMzIDM4LjctNy42OCAyNi0xMS41MiA3OC4yMy0xMS41MiAxNTYuNjkgMCA3Mi4yNiA0LjA1IDEyMi4zNiAxMi4xNiAxNTAuMjkgOC4zIDI2LjQ0IDIzLjg2IDM5LjY2IDQ2LjY4IDM5LjY2IDIyLjM5IDAgMzcuNzQtMTIuMzcgNDYuMDYtMzcuMSA4LjMtMjQuNTEgMTIuNDctNjkuODIgMTIuNDctMTM1Ljl6TTUxNDMuMjQgMjgzLjc1aDIxNi41djU4LjIxaC03NC41MVY3NzcuNUg1MjIwVjM0MS45NmgtNzYuNzZ2LTU4LjJ6Ii8+CiAgICA8cGF0aCBkPSJNNTMzMC45OCAyODMuNzVoMjE2LjV2NTguMjFoLTc0LjUxVjc3Ny41aC02NS4yM1YzNDEuOTZoLTc2Ljc2di01OC4yek01NTU4LjA1IDI4My43NWgxNzYuODR2NTYuMjhoLTExMC4zMnYxNTYuMzloOTcuODZ2NTYuMjdoLTk3Ljg2djE2OC41M2gxMTAuMzJ2NTYuMjhoLTE3Ni44NFYyODMuNzV6TTU3NjkuNzggMjgzLjc1aDYyLjA0bDY2LjE5IDE5Ni45OWMxOS4xOSA1NS42NCAzNi4xNCAxMTUuMDEgNTAuODUgMTc4LjEyLTUuMzQtMzguMTUtOS4yOC03Mi43LTExLjgzLTEwMy42YTEwNTcuNTMgMTA1Ny41MyAwIDAgMS0zLjg0LTg3LjN2LTE4NC4yaDY2LjgzVjc3Ny41aC02Mi4zNWwtNzQuNTItMjIyLjI1YTE0MzYuNjggMTQzNi42OCAwIDAgMS0xOS4zNC02My42NCAxMTUwLjkzIDExNTAuOTMgMCAwIDEtMTYuOC02OC40M2MtLjQxLTIuOTgtMS4xLTYuNjEtMi4wNi0xMC44Ny0uOTctNC4yNy0yLjA5LTkuMTctMy4zNy0xNC43LjY0IDUuNTMgMS4xOCAxMC4yNyAxLjYgMTQuMjIuNDMgMy45NC43NCA3LjMuOTcgMTAuMDdsMy41IDUwLjIgMy41MyA2MS4wOGMuMjEgMy40Mi4zNyA3LjU3LjQ3IDEyLjQ3LjEyIDQuOTEuMTcgMTAuNDUuMTcgMTYuNjRsMy41MSAyMTUuMjFoLTY1LjU1VjI4My43NXoiLz4KICA8L2c+Cjwvc3ZnPgo="
                    />
                </a>
                </div>
                <div class="spacer"></div>
                <div
                    class="fb-share-button"
                    data-href="https://developers.facebook.com/docs/plugins/"
                    data-layout="box_count"
                    data-size="small"
                >
                <div
                    class="fb-share-button"
                    data-href="https://franks.website/artificiellt_osterbotten/?headline{headline}"
                    data-layout="box_count"
                    data-size="small"
                >
                    <a
                        target="_blank"
                        href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Ffranks.website%2Fartificiellt_osterbotten%2F&amp;src=sdkpreparse&amp;headline={headline}"
                        class="fb-xfbml-parse-ignore"
                        >Dela</a
                    >
                </div>
                </div>
            </div>
            <div class="image" style="background-image:url('{photo_url}')">
                <div class="credit">
                    Photo by <a href="{photographer_url}">{photographer}</a> on
                    <a
                        href="https://unsplash.com/?utm_source=artificiellt_osterbotten&utm_medium=referral"
                        >Unsplash</a
                    >
                </div>
            </div>
            <div class="text">
                <h1>{headline}</h1>
                <p class="info">
                    Denna rubrik är genererad av ett neuralt nätverk, upplärt med över
                    25000 tidningsrubriker. Bilden är slumpmässig. Källkod finns
                    <a href="https://github.com/FrankSandqvist/artificiellt-osterbotten">här</a>.
                </p>
                <p class="info">
                    Intresserad av AI och annat nytt och häftigt? Missa då inte
                    <a href="https://www.facebook.com/events/2088754771431983/">
                        NIC Open House
                    </a>!
                </p>
                <br />
                <p class="home">
                <a href="/">
                    franks.website
                </a>
                </p>
            </div>
        </div>
    </body>
    </html>
'''