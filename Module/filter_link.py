class filter_link():
    def join(link):

        link = str(link).replace("https", "http")
        port_none = link.split("/")
        port_none = filter_link.paste_port(port_none)

        return port_none

    def paste_port(link):
        site = link[2]
        site = site + ":80"
        link[2] = site
        full_link = ''
        for i in range(len(link) - 1):
            full_link = full_link + link[i] + "/"
        return full_link
