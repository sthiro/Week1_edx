def main():
    text = input()
    final_text = convert(text)

    print(final_text)


def convert(to):
    to = to.replace(":)","🙂")
    to = to.replace(":(","🙁")

    return to

main()