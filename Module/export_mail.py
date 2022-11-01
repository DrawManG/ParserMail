class join():
    space = "\n"
    def export_to_txt(base,namefile,savepath):
        with open(savepath+namefile+".txt", 'w') as f:
            for end in range(len(base)):
                f.writelines(base[end])
