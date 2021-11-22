from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "kmitl": {"url":"https://new.reg.kmitl.ac.th/admission/",
                    "name": "สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง",
                    "url_img": "https://media.discordapp.net/attachments/912032605845741578/912219519815123004/06be1dd75c2cd4b4becdddee9d32793b8e41172b-7990x4503.png?width=780&height=440"},
        "kmutt": {"url":"https://admission.kmutt.ac.th/",
                    "name": "มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี",
                    "url_img": "https://media.discordapp.net/attachments/912032605845741578/912220558891044864/245323770_4579273088761552_3043661693867198708_n.png?width=706&height=499"},
        "kmunb": {"url":"https://www.admission.kmutnb.ac.th",
                "name":"มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ",
                "url_img": "https://media.discordapp.net/attachments/912032605845741578/912220964627042314/image-1.png?width=780&height=439"},
        "mu": {"url": "https://tcas.mahidol.ac.th/",
                "name": "มหาวิทยาลัยมหิดล",
                "url_img": "https://media.discordapp.net/attachments/912032605845741578/912360426388459621/Calendar65.png?width=499&height=499"},
        "tu": {"url": "https://www.tuadmissions.in.th/",
                "name": "มหาวิทยาลัยธรรมศาสตร์",
                "url_img": "https://media.discordapp.net/attachments/912032605845741578/912362501189013554/2000_2021083019020764.png?width=780&height=244"}

    }
