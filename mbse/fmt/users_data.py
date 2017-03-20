fmt_userhdr = (
    ('hdrsize', 'I'),
    ('recsize', 'I'),
)

fmt_securityrec = (
    ('level', 'I'),
    ('flags', 'I'),
    ('notflags', 'I'),
)

fmt_userrec = (
    ('sUserName', '36s'),
    ('Name', '9s'),
    ('xPassword', 'I'),
    ('sVoicePhone', '20s'),
    ('sDataPhone', '20s'),
    ('sLocation', '28s'),
    ('sAddress', ('41s',)*3),
    ('sDataOfBirth', '12s'),
    ('tFirstLoginDate', 'I'),
    ('tLastLoginDate', 'I'),
    ('Security', None, fmt_securityrec),
    ('sComment', '81s'),
    ('sExpiryDate', '12s'),
    ('ExpirySec', None, fmt_securityrec),
    ('sSex', '8s'),

    ('flags1', 'B'),
    ('flags2', 'B'),

    ('iTotalCalls', 'I'),
    ('iTimeLeft', 'I'),
    ('iConnectTime', 'I'),
    ('iTimeUsed', 'I'),
    ('xScreenLen', 'I'),
    ('tLastPwdChange', 'I'),
    ('xHangUps', 'I'),
    ('Credit', 'I'),
    ('Paged', 'I'),
    ('MsgEditor', 'I'),
    ('LastPktNum', 'I'),
    ('Archiver', '6s'),
    ('iLastFileArea', 'I'),
    ('iLastFileGroup', 'I'),
    ('sProtocol', '21s'),
    ('Downloads', 'I'),
    ('Uploads', 'I'),
    ('UploadK', 'I'),
    ('DownloadK', 'I'),
    ('DownloadKToday', 'I'),
    ('UploadKToday', 'I'),
    ('iLastMsgArea', 'I'),
    ('iTransferTime', 'I'),
    ('iLastMsgGroup', 'I'),
    ('iPosted', 'I'),
    ('iLanguage', 'I'),
    ('sHandle', '36s'),
    ('iStatus', 'I'),
    ('DownloadsToday', 'I'),
    ('CrtDef', 'I'),
    ('Protocol', 'I'),
    ('flags3', 'B'),
    ('Password', '15s'),
    ('Charset', 'I'),
    ('OLRext', 'I'),
    ('OLRlast', '12s'),
)

# flags2
FLAG_HIDDEN = 1
FLAG_HOTKEYS = 1 << 1
FLAG_XGRAPHMODE = 1 << 2
FLAG_DELETED = 1 << 3
FLAG_NEVERDELETE = 1 << 4
FLAG_XCHAT = 1 << 5
FLAG_LOCKEDOUT = 1 << 6
FLAG_DONOTDISTURB = 1 << 7

# flags2
FLAG_CLS = 1
FLAG_MORE = 1 << 1
FLAG_XFSMSGED = 1 << 2
FLAG_MAILSCAN = 1 << 3
FLAG_GUEST = 1 << 4
FLAG_OL_EXTINFO  = 1 << 5

# flags3
FLAG_IEMSI = 1
FLAG_IEMNU = 1 << 1
FLAG_IETAB = 1 << 2
FLAG_IEASCII8 = 1 << 3
FLAG_IENEWS = 1 << 4
FLAG_IEFILE = 1 << 5
FLAG_EMAIL = 1 << 6
FLAG_FSEMACS = 1 << 7
