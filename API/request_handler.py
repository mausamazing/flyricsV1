import acoustid
import json
def lookup_acoustid(fingerprint, duration):
    global artist_name
    global song_name
    try:
        # Perform the lookup using the AcoustID API
        result = acoustid.lookup('5lkdThuCBA8', fingerprint, duration, meta='recordings')#meta='recordings releasegroups compress'

        # # Print the entire result for debugging
        # print("Full Result:", result)

        # Ensure result is not empty and process each item
        if result:
            artist_name = result['results'][0]['recordings'][0]['artists'][0]['name']
            print(artist_name)
            song_name = result['results'][0]['recordings'][0]['title']
            print(song_name)

            # for item in result:
            #     print(item['status'])
            #     # Check if item is a dictionary (expected format)
            #     if isinstance(item, dict):
            #         score = round(float(item['score']) * 100)  # Convert score to float, multiply by 100, and round
            #         recording_id = item['id']
            #         title = item['title']
            #         artist = item['artist']
            #         status = item['status']

            #         print(f"Score: {score}%, Recording ID: {recording_id}, Title: {title}, Artist: {artist}")
            #     else:
            #         print("Unexpected item format:", item)
    except Exception as e:
        print(e)

# # Example fingerprint and duration (in seconds)
# fingerprint = 'AQADtGoWNZIW4RnRPD6S3UX6EM_xbXkgL9GDc-gxZQeXhBgPez-uG8efQSdTFk-S49rxHVY8409O4Elv_IGX5Uj-ILeRhwmOMBb6qMKj5qhVNN9x0Vqg5ketommSHcdtlMqEZtlT_IL26EZz4pHy48su3E-M7cVzXFGSvegTTPn04SGxO_hzcErQD8mi9UGe7cd18EP64zFikQ4-5RWoHCdffFmKdDqU68ipHP2DbeHhHU-DJ4OrI1GepYhOB0_wbUeVCX1yHMdTIlkqHnlz4UC9HU_EGO8RLiGa6MCTHE3cHdqPPGJQEo7y44mwVRf65EhOIs-S4ccTNMyGiWSOZyma0E9x6kh6hHGU4Eoe4z_uDP9xyUfDRM8Q8kZylD2cJEc_xcFX_Icfyjj1Y1SObNm8DFpOhD-e5cITHf6QB2y4I_c6PAtzOMd5sFHCIb2g70XOnKjawM9w7Rks1gluONWRzCKyJ0qxKw_uHM_xJclRSjeO57gLN43h2uhxIX0IlTnxJOKDi2EVpA-eHN-D2IV4GU8jKziXbEgVDjtCHUy6JUXy4szx6CiZEUzyDGN84U_RB1ciJJMn5I58PHnw4ccf1JKOZGmSHLGCmwwabR4qJaEq4hf-obl2o05SPDn-oo8HLU1wPsfRPA_65_im48qQE2IoIs8cnEwo7EezU6if48J1ZPkS6AorROZx5SiPH9-IJ3zQRJEQWtCPHNWHKUnoBmyWB3tQf2ge4Do-fUiuSJ8QZ86B5uiTC8kfIa8uPFvwWxH6B02OXCe0F6Gf4NvwHj-uoN4jpBmX9Ki3Zvh2oZuGNG-I62ie48eZZB4alalQHZeOK8kCcwt-4VtxHZGSKJEPKRQRHruFS0ebHGWXoXlyHKFYEaKYHNeJNNKN90jHHbUpPNqEHlqeG_eF8zg5I49DeBkTnFGOMNWPPoM-5E4ToYmYD11y414yKFcTCvxSOAlvjErS9PiDonk44Qp-XEmP5IlyhAqaHM_xRzgT5E1yQT3yHvmD_4X4BTnxhTjzFO-OFw-qH4cvlMeF_2jWKDeSXwijFF9RkgmaNHnwC3oiCtsZPAYnjsIV7MeNZB6NdEe7o3uOK1OOE32M58gPRY4jhKnA-4FzPriio8mRBU-UCaqX6ci4H8ezeMKRV4LXpcZ3ND-6LDmaWEoRNuLx_JjyHi2PSz-aNOHx6YKfwqHQ9yS-5bgo0jAXTcKP-By05rB5ROvxo9GUJR_e6MIdCs21oR_ahbngI78gZqGyBT2RZzm-HN-x7kZ5NJKSDxdfTIkTpeiRhQyUVUR-o3GOPjua5Cm-pbhO_AgfNGcOdYuOHzuN-Oh9-Lng9_jhL5_Qow9TNN-L5EuPUFqjgonKEn2Zo3kr4NqRN9AZJRXxUQwOLWrRJ7nxww5TvDnELFyRH4-xcTSuHY3TDxV3oVGNH03F53h6XJmISkyOhtskvDySdVmGs9gbC6FodHPyovmOd6g5ofmDPkoO8zp6IhRFQ6RSoyvqXYhaohR-Cs2OWtE3dCKmxDX4HbmyQNE15CqFPg-auOh6fFLxHLnQPDm0UsGvYOXxhwh7OA3zwVwWo9fx_ELz8KiPPktVIVnICbl0OE11nGhCZU6CPseP5IlyIQ9TXKEePB_iH9q3oqly8BcR5kcodVCkHGG6GQ-THqdxbTmei8PhikHloBEbCl-IP8zRPIobfDnSSzGuwC96Hy-RRA_RpNHxCO12eFIu-MdV3D_SJ4e28EQbHeWSFe8KpWjqoVwYB_J2NHEyDRNxZWByKRXKHf0DMaMwRRre5Dhx5hLKo3mKj1izF4cQfieeo-Q-0D3eS4N__EQ5sTq0LCyamDn6meiaH43TLMGJzznCR0UyJj5eJQXPBo3oo39wNBPCLis8_sjYHD-aSSXRSsNEWFP2wSfqwaqOJ0ocXD8qZVKCZv0R3tjiRBmHvBe87ej0EDl5aG-DuC3x6fhyNPvx9cF1oTmDcCWhWbQRchKeiFqwXgXSXoae_Lh8bGqUEPcHKVYW-MONKc-4QEvcoWNy3EYeXfjR_IikSceJ69cgZIG_HH50CmVUXJdQiVlONMdzdNQSHgmXHbHWyIGfozkTxsFbCuimHtWPPFnB6sGFpuOh6kHT41TRTC0Rnrh4MHp8NFx2nJgyRUPPpBt8Hld-2LXwRUesZyiz6IKWLw9qMXiCr1yg9cHFQ4u8I1SbGPdRPpLg3zAnmZieMageYeNR5wg3HW9mEVqPo2kaI7Sk42gS85gu8EOfrphy5MebqAs-Hd90nFD-oD4RKd6O8cfzD98ThM0hJWeQZ4edHvw_NOs69MdFhNm0FMk0lsEj9cH1wnkXTGcaNJ5w49kxJj-ScxxKRMOjHEdjO0GcEk2k6QgZ5jiPKQdDZseXhDkmJTqa73g4HFdw9Xgi8Ui-HKE-NMlxOjglE49L5FaOb8eUC7V-_EHPENGq4yd8zkZ_4juOb0Pto8n24RReCqEWrtBphFwk4RKPak4sNL-RH5rHI3p2cKphTkT4YW4EfUHJHGlW9DWOOtGo4EeXHz9-5KYliA4TRJ9xwVHycOjClGh8E28Y5IkOKZuG8MaPp4_wCFPiFn1y9IoRJubRJxHCJJGDHzf84BJPNE6W49Rh1fBzVHTc4dHwoxkTdNqKPIRmXUNcoo3jYPzRaMp6VA2TC-fRa4M_tMt09IQ_xJR0QqSaDeFyHGuTB-_QH94ihRye7AnG-GiuEdljKKJ0pLxgf8FzNEkrfAtOfEku_EOYQ9OPC8d-hP3h14K5HN_h50RJXuiZg8lnJO-FkBmHJiLzofuyonmWBi-u4Mou5Duhlw0eHtdhJywuHU0eo2NypJEkJXgmfDymcIxRD1-6Eu6OfnDSFE2o4zYAYIQATAJBgCBACEcgFYBIQgADACCAnATOICcIEAQQwERSEghBFQCGAKOEAUAD4hwRBBABAIBYESKIIcIwBAxRAjmqrDAMSKAQZAApBChgIBEhFFWECQOQAg4gJgQySDBDgDAKOGS4AQAEwgAxgBHlmEGGeiQAkERBYgwAQlFKDABWECAZa4SZBoAAACGDCBDGCEigEYYgBxAgyCABglGIEAgkAEQRIwBAZBgEBBAIKAKkUUAhIwk1BjIDgXIADCSYYgYBIQgQwgFgjCBAScSEAg04QAQgQjEJDIKAIkGIYoAo54iBgIDGgDBCKAUMMAIBRYARQBkCgTJEIAYYNMQAZhlhhhBgBDIKACIUKMQIAgKxwokhgDDIIKQQIEhJxhQwBADFiJLGACAUaYABTxBQRAlCmAFAEGIAEQgAgAAQFEABgCGAICKEVkIAhAADghBCFAFICAIUYQoBQYQjFhhggIFACAWEEIwAwAgABgJBgVCMUkKIAQAAZZATAhAgEABEEAC0UIAAAgwiwhjAmDcCQCMFEAYoAoBgQhCEFUAGEQSEcEYAQwxgVAFGAAMiEUEAIwAhILAwVBBFMDDCIKEQRMAJBAwkRCCgADDMEUmEAgwBo4jwAhBDkCBGIYAYBQApZAgQyggDBCIUIAKYEcAAIoERgAAAqAIGKMCcEkQAIIAAhAGAmCEKCAAEQIoZAYUwQhkggAAOGYCIAAAxAgBGCAiBFBFEComBExQAghEQAAhskBKAAgGU0IAQAICwBAmFABCACQAEA4wwBhADgApgMUMCAQElY4gI4QRFgDCGFAMMGOmUMGQoIgQRFAghlEECQQIAYMQIF4hSxjpDgADQEOCoBYQQgIBDQCphBAHIGCAkFRABpAQhBBCFCCMAEkOcAkgARgACSBkglABCIYCAgkgoAowAhimjmHGESawA'

# duration = 208  # Duration of the audio in seconds

# # Perform the lookup
# lookup_acoustid(fingerprint, duration)
