import os
from subprocess import Popen, PIPE

def extract_featues(output):
    tuples = []
    obj_subsection = bytes(output[2])
    obj_subsection = obj_subsection.replace(b'obj', b'')
    obj_subsection = obj_subsection.replace(b' ', b'')
    obj_subsection = obj_subsection.replace(b'\\n', b'')
    obj_subsection = obj_subsection.decode('UTF-8')
    try:
        obj = int(obj_subsection)
        tuples.append(obj)
    except ValueError:
        obj = 10
        tuples.append(obj)
        pass

    endobj_subsection = bytes(output[3])
    endobj_subsection = endobj_subsection.replace(b'endobj', b'')
    endobj_subsection = endobj_subsection.replace(b' ', b'')
    endobj_subsection = endobj_subsection.replace(b'\\n', b'')
    endobj_subsection = endobj_subsection.decode('UTF-8')
    try:
        obj = int(endobj_subsection)
        tuples.append(obj)
    except ValueError:
        obj = 10
        tuples.append(obj)
        pass

    stream_subsection = bytes(output[4])
    stream_subsection = stream_subsection.replace(b'stream', b'')
    stream_subsection = stream_subsection.replace(b' ', b'')
    stream_subsection = stream_subsection.replace(b'\\n', b'')
    stream_subsection = stream_subsection.decode('UTF-8')
    try:
        stream = int(stream_subsection)
        tuples.append(stream)
    except ValueError:
        stream = 3
        tuples.append(stream)
        pass

    endstream_subsection = bytes(output[5])
    endstream_subsection = endstream_subsection.replace(b'endstream', b'')
    endstream_subsection = endstream_subsection.replace(b' ', b'')
    endstream_subsection = endstream_subsection.replace(b'\\n', b'')
    endstream_subsection = endstream_subsection.decode('UTF-8')
    try:
        endstream = int(endstream_subsection)
        tuples.append(endstream)
    except ValueError:
        endstream = 3
        tuples.append(endstream)
        pass


    xref_subsection = bytes(output[6])
    xref_subsection = xref_subsection.replace(b'xref', b'')
    xref_subsection = xref_subsection.replace(b' ', b'')
    xref_subsection = xref_subsection.replace(b'\\n', b'')
    xref_subsection = xref_subsection.decode('UTF-8')
    try:
        xref = int(xref_subsection)
        tuples.append(xref)
    except ValueError:
        xref = 1
        tuples.append(xref)
        pass

    trailer_subsection = bytes(output[7])
    trailer_subsection = trailer_subsection.replace(b'trailer', b'')
    trailer_subsection = trailer_subsection.replace(b' ', b'')
    trailer_subsection = trailer_subsection.replace(b'\\n', b'')
    trailer_subsection = trailer_subsection.decode('UTF-8')
    try:
        trailer = int(trailer_subsection)
        tuples.append(trailer)
    except ValueError:
        trailer = 1
        tuples.append(trailer)
        pass

    startxref_subsection = bytes(output[8])
    startxref_subsection = startxref_subsection.replace(b'startxref', b'')
    startxref_subsection = startxref_subsection.replace(b' ', b'')
    startxref_subsection = startxref_subsection.replace(b'\\n', b'')
    startxref_subsection = startxref_subsection.decode('UTF-8')
    try:
        startxref = int(startxref_subsection)
        tuples.append(startxref)
    except ValueError:
        startxref = 1
        tuples.append(startxref)
        pass

    Page_subsection = bytes(output[9])
    Page_subsection = Page_subsection.replace(b'/Page', b'')
    Page_subsection = Page_subsection.replace(b' ', b'')
    Page_subsection = Page_subsection.replace(b'\\n', b'')
    Page_subsection = Page_subsection.decode('UTF-8')
    try:
        Page = int(Page_subsection)
        tuples.append(Page)
    except ValueError:
        Page = 1
        tuples.append(Page)
        pass

    Encrypt_subsection = bytes(output[10])
    Encrypt_subsection = Encrypt_subsection.replace(b'/Encrypt', b'')
    Encrypt_subsection = Encrypt_subsection.replace(b' ', b'')
    Encrypt_subsection = Encrypt_subsection.replace(b'\\n', b'')
    Encrypt_subsection = Encrypt_subsection.decode('UTF-8')
    try:
        Encrypt = int(Encrypt_subsection)
        tuples.append(Encrypt)
    except ValueError:
        Encrypt = 0
        tuples.append(Encrypt)
        pass

    ObjStm_subsection = bytes(output[11])
    ObjStm_subsection = ObjStm_subsection.replace(b'/ObjStm', b'')
    ObjStm_subsection = ObjStm_subsection.replace(b' ', b'')
    ObjStm_subsection = ObjStm_subsection.replace(b'\\n', b'')
    ObjStm_subsection = ObjStm_subsection.decode('UTF-8')
    try:
        ObjStm = int(ObjStm_subsection)
        tuples.append(ObjStm)
    except ValueError:
        ObjStm = 0
        tuples.append(ObjStm)
        pass


    JS_subsection = bytes(output[12])
    JS_subsection = JS_subsection.replace(b'/JS', b'')
    JS_subsection = JS_subsection.replace(b' ', b'')
    JS_subsection = JS_subsection.replace(b'\\n', b'')
    JS_subsection = JS_subsection.decode('UTF-8')
    try:
        JS = int(JS_subsection)
        tuples.append(JS)
    except ValueError:
        JS = 1
        tuples.append(JS)
        pass

    JavaScript_subsection = bytes(output[13])
    JavaScript_subsection = JavaScript_subsection.replace(b'/JavaScript', b'')
    JavaScript_subsection = JavaScript_subsection.replace(b' ', b'')
    JavaScript_subsection = JavaScript_subsection.replace(b'\\n', b'')
    JavaScript_subsection = JavaScript_subsection.decode('UTF-8')
    try:
        JavaScript = int(JavaScript_subsection)
        tuples.append(JavaScript)
    except ValueError:
        JavaScript = 1
        tuples.append(JavaScript)
        pass

    AA_subsection = bytes(output[14])
    AA_subsection = AA_subsection.replace(b'/AA', b'')
    AA_subsection = AA_subsection.replace(b' ', b'')
    AA_subsection = AA_subsection.replace(b'\\n', b'')
    AA_subsection = AA_subsection.decode('UTF-8')
    try:
        AA = int(AA_subsection)
        tuples.append(AA)
    except ValueError:
        AA = 0
        tuples.append(AA)
        pass

    OpenAction_subsection = bytes(output[15])
    OpenAction_subsection = OpenAction_subsection.replace(b'/OpenAction', b'')
    OpenAction_subsection = OpenAction_subsection.replace(b' ', b'')
    OpenAction_subsection = OpenAction_subsection.replace(b'\\n', b'')
    OpenAction_subsection = OpenAction_subsection.decode('UTF-8')
    try:
        OpenAction = int(OpenAction_subsection)
        tuples.append(OpenAction)
    except ValueError:
        OpenAction = 1
        tuples.append(OpenAction)
        pass

    AcroForm_subsection = bytes(output[16])
    AcroForm_subsection = AcroForm_subsection.replace(b'/AcroForm', b'')
    AcroForm_subsection = AcroForm_subsection.replace(b' ', b'')
    AcroForm_subsection = AcroForm_subsection.replace(b'\\n', b'')
    AcroForm_subsection = AcroForm_subsection.decode('UTF-8')
    try:
        AcroForm = int(AcroForm_subsection)
        tuples.append(AcroForm)
    except ValueError:
        AcroForm = 0
        tuples.append(AcroForm)
        pass


    JBIG2Decode_subsection = bytes(output[17])
    JBIG2Decode_subsection = JBIG2Decode_subsection.replace(b'/JBIG2Decode', b'')
    JBIG2Decode_subsection = JBIG2Decode_subsection.replace(b' ', b'')
    JBIG2Decode_subsection = JBIG2Decode_subsection.replace(b'\\n', b'')
    JBIG2Decode_subsection = JBIG2Decode_subsection.decode('UTF-8')
    try:
        JBIG2Decode = int(JBIG2Decode_subsection)
        tuples.append(JBIG2Decode)
    except ValueError:
        JBIG2Decode = 0
        tuples.append(JBIG2Decode)
        pass

    RichMedia_subsection = bytes(output[18])
    RichMedia_subsection = RichMedia_subsection.replace(b'/RichMedia', b'')
    RichMedia_subsection = RichMedia_subsection.replace(b' ', b'')
    RichMedia_subsection = RichMedia_subsection.replace(b'\\n', b'')
    RichMedia_subsection = RichMedia_subsection.decode('UTF-8')
    try:
        RichMedia = int(RichMedia_subsection)
        tuples.append(RichMedia)
    except ValueError:
        RichMedia = 0
        tuples.append(RichMedia)
        pass

    Launch_subsection = bytes(output[19])
    Launch_subsection = Launch_subsection.replace(b'/Launch', b'')
    Launch_subsection = Launch_subsection.replace(b' ', b'')
    Launch_subsection = Launch_subsection.replace(b'\\n', b'')
    Launch_subsection = Launch_subsection.decode('UTF-8')
    try:
        Launch = int(Launch_subsection)
        tuples.append(Launch)
    except ValueError:
        Launch = 0
        tuples.append(Launch)
        pass

    EmbeddedFile_subsection = bytes(output[20])
    EmbeddedFile_subsection = EmbeddedFile_subsection.replace(b'/EmbeddedFile', b'')
    EmbeddedFile_subsection = EmbeddedFile_subsection.replace(b' ', b'')
    EmbeddedFile_subsection = EmbeddedFile_subsection.replace(b'\\n', b'')
    EmbeddedFile_subsection = EmbeddedFile_subsection.decode('UTF-8')
    try:
        EmbeddedFile = int(EmbeddedFile_subsection)
        tuples.append(EmbeddedFile)
    except ValueError:
        EmbeddedFile = 0
        tuples.append(EmbeddedFile)
        pass

    XFA_subsection = bytes(output[21])
    XFA_subsection = XFA_subsection.replace(b'/XFA', b'')
    XFA_subsection = XFA_subsection.replace(b' ', b'')
    XFA_subsection = XFA_subsection.replace(b'\\n', b'')
    XFA_subsection = XFA_subsection.decode('UTF-8')
    try:
        XFA = int(XFA_subsection)
        tuples.append(XFA)
    except ValueError:
        XFA = 0
        tuples.append(XFA)
        pass

    colors_subsection = bytes(output[22])
    colors_subsection = colors_subsection.replace(b'/Colors > 2^24', b'')
    colors_subsection = colors_subsection.replace(b' ', b'')
    colors_subsection = colors_subsection.replace(b'\\n', b'')
    colors_subsection = colors_subsection.decode('UTF-8')
    try:
        colors = int(colors_subsection)
        tuples.append(colors)
    except ValueError:
        colors = 0
        tuples.append(colors)
        pass

    return tuples


def feature_extraction(filepath):
    features = []
    command_to_execute = 'python3 pdfid.py ' + filepath
    stdout = Popen(command_to_execute, shell=True, stdout=PIPE).stdout
    output = stdout.readlines()
    if len(output) == 24:
        features.append(extract_featues(output))
    return features
