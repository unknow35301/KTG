import KTG
while True:
    try:
        KTG.main()
    except SystemExit:
        break
    except Exception:
        pass