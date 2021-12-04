from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
       "ku": {"url":"https://admission.ku.ac.th/",
              "name": "มหาวิทยาลัยเกษตรศาสตร์",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912967371235401728/534869f1d3bd38e9f79516a18c437f6a9d823c18-1440x1019.png?width=653&height=462"},
        
       "buu": {"url":"https://regservice.buu.ac.th/",
              "name": "มหาวิทยาลัยบูรพา",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912967748945080340/5dc23c19087987e8a192deded68705db490411ba-1440x1154.png?width=577&height=462"},
        
       "kmitl": {"url":"https://new.reg.kmitl.ac.th/admission/#/",
              "name": "สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912968632810737705/06be1dd75c2cd4b4becdddee9d32793b8e41172b-7990x4503.png?width=705&height=397"},

       "tu": {"url": "https://www.tuadmissions.in.th/",
              "name": "มหาวิทยาลัยธรรมศาสตร์",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912981213080326154/c9b5925075e9f38eed0986619ae2e3fe349298be-2000x2000.png?width=469&height=469"},
       
       "cu": {"url": "http://www.admissions.chula.ac.th/",
              "name": "จุฬาลงกรณ์มหาวิทยาลัย",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912982253452271616/62d9071fbe423809ca049514361ca97e2973020b-1338x766.png?width=705&height=404"},
       
       "swu": {"url": "https://admission.swu.ac.th/admissions2/",
              "name": "มหาวิทยาลัยศรีนครินทรวิโรฒ",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912982286310441000/6c54bd2c29c58f7edc24683ee52a04de069fde3f-2048x672.png?width=705&height=231"},
       
       "psu": {"url": "https://e-admission.psu.ac.th/",
              "name": "มหาวิทยาลัยสงขลานครินทร์",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912982589273436160/4bd1a9aca05a53b858e4ab5d5992f487204d3bc0-3200x1800.png?width=705&height=397"},
       
       "pnru": {"url": "https://admission.pnru.ac.th/home/info",
              "name": "มหาวิทยาลัยราชภัฏพระนคร",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912982689462771752/9d8c1ea19f658de4dfd73d7ab7cf68b5ca9a08f0-2000x2000.png?width=469&height=469"},
       
       "su": {"url": "https://www.admission.su.ac.th/",
              "name": "มหาวิทยาลัยศิลปากร",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912982706827173888/8426cc7f351f73325af774b067044c6d9fe1c724-2000x1756.png?width=534&height=469"},
       
       "skru": {"url": "https://www.skru.ac.th/th/bachelor/pregis",
              "name": "มหาวิทยาลัยราชภัฏสงขลา",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912983829449408542/a80ce47f8c3bd4284ec76efa74f669c91924853f-1000x700.png?width=669&height=468"},
       
       "rmutsb": {"url": "https://admissions.rmutsb.ac.th/web_admis/",
              "name": "มหาวิทยาลัยเทคโนโลยีราชมงคลสุวรรณภูมิ",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912984100493733919/e4c6b64b29b6722a5ce2c6db23f07d84eb9a512c-3491x2533.png?width=646&height=469"},
       
       "msu": {"url": "https://admission.msu.ac.th/",
              "name": "มหาวิทยาลัยมหาสารคาม",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912983722666627133/1c40b0c6514173748c51ba97e8afc0f25ea6ef0c-1800x1080.png?width=705&height=423"},
       
       "mfu": {"url": "https://admission.mfu.ac.th/admission-home.html",
              "name": "มหาวิทยาลัยแม่ฟ้าหลวง",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912985245127696434/3e9deb45cbe19de913b8ed0474f0ea8ca96642de-3508x2675.png?width=615&height=469"},
       
       "hu": {"url": "https://admission.hu.ac.th/",
              "name": "มหาวิทยาลัยหาดใหญ่",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912987251015835658/ce5de1cd3bbb7026169b96cc7213874c6b2246bd-1920x1080.png?width=705&height=397"},
       
       "tsu": {"url": "https://admission.tsu.ac.th/admission/applicant/projectlist.jsp",
              "name": "มหาวิทยาลัยทักษิณ",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912987497552826388/6b99238ae5f289e19028cc72994f835024306760-5000x3334.png?width=704&height=469"},
       
       "ssru": {"url": "https://admission.ssru.ac.th/isqy01",
              "name": "มหาวิทยาลัยราชภัฏสวนสุนันทา",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912987557959184424/3510927001eec62760aa18e7212560527451c8bb-1568x1045.png?width=704&height=469"},
       
       "sut": {"url": "http://sutgateway.sut.ac.th/admissions2021/",
              "name": "มหาวิทยาลัยเทคโนโลยีสุรนารี",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912988531947884554/90ef3349ba53f02ff28d94d98c95db1453e8f61d-4000x2257.png?width=705&height=398"},
       
       "up": {"url": "https://admission.up.ac.th/63/",
              "name": "มหาวิทยาลัยพะเยา",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912992227612037181/811209646fa531bbe24fc65b6cc13d829b577a4d-2000x1333.png?width=704&height=469"},
       
       "mju": {"url": "http://www.admissions.mju.ac.th/www/",
              "name": "มหาวิทยาลัยแม่โจ้",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912994572915834910/b804aee5368de5583ececccc80ac564bf45022e0-3417x1300.png?width=705&height=268"},
       
       "vru": {"url": "http://ent.vru.ac.th/Webregister/pages/Homepages.php",
              "name": "มหาวิทยาลัยราชภัฏวไลยอลงกรณ์",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912993834059841566/24a42bd4fe557b795dd90f0ebd7834070c573f1f-1280x720.png?width=705&height=397"},
       
       "cmu": {"url": "https://www1.reg.cmu.ac.th/ugradapply/",
              "name": "มหาวิทยาลัยเชียงใหม่",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912993733425889290/d8930b5e7361b16cdf78d579b0645599f7376a2f-2481x3508.png?width=332&height=469"},
       
       "cdti": {"url": "https://reg.cdti.ac.th/registrar/appquotalist.asp",
              "name": "สถาบันเทคโนโลยีจิตรลดา",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912993637745430588/4e5890b83b13ea397f2996896acadebdc4c19432-1107x840.png?width=618&height=469"},
       
       "rmutr": {"url": "https://tcas.rmutr.ac.th/",
              "name": "มหาวิทยาลัยเทคโนโลยีราชมงคลรัตนโกสินทร์",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912995303894974484/ac1205a8585551f3ac9d18913621193d36177ddb-1418x1157.png?width=575&height=469"},
       
       "rmutp": {"url": "https://reg.rmutp.ac.th/registrar/apphome.asp",
              "name": "มหาวิทยาลัยเทคโนโลยีราชมงคลพระนคร",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912997814496284702/d7e7ae25af76e10ecf6b8272894d60aebd39355c-5334x3405.png?width=705&height=450"},
       
       "nu": {"url": "https://www.admission.nu.ac.th/",
              "name": "มหาวิทยาลัยนเรศวร",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912998033225052180/9e530f813682f52782167da5ee5ee00c8333d85c-2250x3250.png?width=325&height=469"},
       
       "kucsc": {"url": "https://misreg.csc.ku.ac.th/admission/",
              "name": "มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตเฉลิมพระเกียรติ จังหวัดสกลนคร",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912998038983806996/bd2291fdf749cf767070b79f08f855958bbac5a0-2160x1647.png?width=615&height=469"},

       "rmutto": {"url": "https://academic.rmutto.ac.th/?page_id=25",
              "name": "มหาวิทยาลัยเทคโนโลยีราชมงคลตะวันออก",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/912999949694795776/c0181b9c2fb6d3f837047207194232665b0d79d8-1919x1279.png?width=704&height=469"},
       
       "kukps": {"url": "https://admission.kps.ku.ac.th/kpsadm/",
              "name": "มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตกำแพงแสน",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913001543945584690/bcfba42c6f53a3d6e4a1613470503e5d4d5c6e22-1606x1020.png?width=705&height=448"},
       
       "psru": {"url": "https://reg.psru.ac.th/reg2018/",
              "name": "มหาวิทยาลัยราชภัฏพิบูลสงคราม",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913001813379264522/2a6c2c63066399fd5e293a93b4788189fac57c2f-3937x2215.png?width=705&height=397"},
       
       "rmutt": {"url": "https://apply.rmutt.ac.th/",
              "name": "มหาวิทยาลัยเทคโนโลยีราชมงคลธัญบุรี",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913002083291131914/b2ce90b0acc98391e68b0fe3922b132279585dc3-2500x1375.png?width=705&height=388"},
       
       "slc": {"url": "https://www.slc.ac.th/2018/applystudent/",
              "name": "วิทยาลัยเซนต์หลุยส์",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913002668966944768/2b8040f644aeee365a94087eec18bbd29527ee70-1895x1393.png?width=638&height=469"},
       
       "kusrc": {"url": "https://admission.ku.ac.th/",
              "name": "มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตศรีราชา",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913003012467863603/aa73645898c632e8da72f83335d5f08304aec23b-1721x2435.png?width=331&height=469"},
       
       "rmuti": {"url": "https://surin-ess.rmuti.ac.th/eAdmission/eApplicant/AdmissionLogin.aspx",
              "name": "มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913043780737839144/22cb101cf8f7464a0cbff1f01f303ac014ea0a97-3508x2480.png?width=664&height=469"},
       
       "ntc": {"url": "http://northern.ac.th/",
              "name": "วิทยาลัยนอร์ทเทิร์น",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913043656854868008/0f122331955ae26463556221f2bee2ce6fd961e0-1684x1191.png?width=663&height=469"},
       
       "pi": {"url": "http://admission.pi.in.th/admission/",
              "name": "สถาบันพระบรมราชชนก",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913044039769686066/c12de6de9bb809bec6138802535fc40f1624e44b-2354x1754.png?width=630&height=469"},
       
       "pgvim": {"url": "http://www.pgvim.ac.th/admission/",
              "name": "สถาบันดนตรีกัลยาณิวัฒนา",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913044803095248896/0f5b052c1332b2cca9aabd9ab50216f0f015f8e0-2000x1125.png?width=705&height=397"},
       
       "ru": {"url": "http://www.iregis2.ru.ac.th/",
              "name": "มหาวิทยาลัยรามคำแหง",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913045093798273074/ac7bc539b6fc8b42dcdfe80ae04131a2b8df9198-1486x2220.png?width=314&height=469"},
       
       "npu": {"url": "http://admission.npu.ac.th/admis/",
              "name": "มหาวิทยาลัยนครพนม",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913045456714625064/b5bbbd4956e564a067ccad9680c07a543c3d37d0-4084x2816.png?width=680&height=469"},
       
       "kmutt": {"url": "https://admission.kmutt.ac.th/",
              "name": "มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913045137729417246/4c131bee0323e330e4475919bc72581724267395-3508x2480.png?width=664&height=469"},
       
       "mu": {"url": "https://tcas.mahidol.ac.th/",
              "name": "มหาวิทยาลัยมหิดล",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913045302095773776/6788ee7c29c45bb96a5f0442b91a13300cd50e04-2048x2048.png?width=469&height=469"},
       
       "cru": {"url": "https://www.chandra.ac.th/",
              "name": "มหาวิทยาลัยราชภัฏจันทร์เกษม",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913046451435732992/19c8a79b2ae06bb44fac4d0d9ec35bc2689ca101-1250x1563.png?width=375&height=469"},
       
       "nmu": {"url": "https://reg1.nmu.ac.th/registrar/apphome.asp",
              "name": "มหาวิทยาลัยนวมินทราธิราช",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913046512169279561/197a32eac616870da19c642d8ff83529c210d0f1-2000x1667.png?width=562&height=468"},
       
       "pnumc": {"url": "https://admission.pnu.ac.th/",
              "name": "มหาวิทยาลัยนราธิวาสราชนครินทร์",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913046504766332989/9a911153d55b44aa43f6389f88ad7d468a6989c0-1521x1076.png?width=663&height=469"},
       
       "bsru": {"url": "http://202.29.54.207/dev3/admission/index.php",
              "name": "มหาวิทยาลัยราชภัฏบ้านสมเด็จเจ้าพระยา",
              "url_img": "https://media.discordapp.net/attachments/912967297013002281/913046795494494208/fa0572d7d9c89820758251f9305356315ce454bc-4097x2827.png?width=680&height=469"},
       "kku": {"url": "https://admissions.kku.ac.th/",
              "name": "มหาวิทยาลัยขอนแก่น",
              "url_img": "https://cdn.discordapp.com/attachments/910079938936315978/916528100676886558/256194157_603047997676461_2938166091073837676_n-1.png"}
       
       
    }
