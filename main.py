#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################################################################
# password manager webpage - (c) 2021 Paul Deiss - Use at your own risk, no warranty!
########################################################################################################################


from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
