' VBA function which changes big to little endian
' reverses 1 byte (2 hex number pair)
' e.g changes 480000074B26E42D to 2DE4264B07000048
'
Public Function strReverse_Character_Pairs(ByVal strValue As String) As String

    Dim lngLoop                                           As Long
    Dim strReturn                                         As String
  
    strReturn = ""
  
    For lngLoop = Len(strValue) - 1& To 1& Step -2&
        strReturn = strReturn & Mid$(strValue, lngLoop, 2)
    Next lngLoop
  
    strReverse_Character_Pairs = strReturn  
  End Function