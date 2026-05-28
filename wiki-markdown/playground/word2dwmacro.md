* Copy the code from below, and save it as Word2Doku.bas
* Start Word
* Bring up the Visual Basic Editor (Tools->Macro->Visual Basic Editor or Alt+F11).
* From the VBE, import the macro library (File->Import File...) and select the file you downloaded.
<code>
Attribute VB_Name = "Word2DokuWikiv3"

Sub Word2DokuWiki()
    Application.ScreenUpdating = False
    ReplaceQuotes
    DokuWikiEscapeChars
    DokuWikiConvertHyperlinks
    DokuWikiConvertH1
    DokuWikiConvertH2
    DokuWikiConvertH3
    DokuWikiConvertH4
    DokuWikiConvertH5
    DokuWikiConvertItalic
    DokuWikiConvertBold
    DokuWikiConvertUnderline
    DokuWikiConvertStrikeThrough
    DokuWikiConvertSuperscript
    DokuWikiConvertSubscript
    DokuWikiConvertLists
    DokuWikiConvertTable
    UndoDokuWikiEscapeChars
    ' Copy to clipboard
   ActiveDocument.Content.Copy
   Application.ScreenUpdating = True
End Sub

Private Sub DokuWikiConvertH1()
    ReplaceHeading wdStyleHeading1, "======"
End Sub

Private Sub DokuWikiConvertH2()
    ReplaceHeading wdStyleHeading2, "====="
End Sub

Private Sub DokuWikiConvertH3()
    ReplaceHeading wdStyleHeading3, "===="
End Sub

Private Sub DokuWikiConvertH4()
        ReplaceHeading wdStyleHeading4, "==="
End Sub

Private Sub DokuWikiConvertH5()
    ReplaceHeading wdStyleHeading5, "=="
End Sub

Private Sub DokuWikiConvertH6()
    ReplaceHeading wdStyleHeading5, "="
End Sub

Private Sub DokuWikiConvertBold()
    ActiveDocument.Select
    With Selection.Find
        .ClearFormatting
        .Font.Bold = True
        .Text = ""
        .Format = True
        .MatchCase = False
        .MatchWholeWord = False
        .MatchWildcards = False
        .MatchSoundsLike = False
        .MatchAllWordForms = False
        .Forward = True
        .Wrap = wdFindContinue
       
        Do While .Execute
            With Selection
                If Len(.Text) > 1 And InStr(1, .Text, vbCr) Then
                    ' Just process the chunk before any newline characters
                    ' We'll pick-up the rest with the next search
                    .Collapse
                    .MoveEndUntil vbCr
                End If
                                      
                ' Don't bother to markup newline characters (prevents a loop, as well)
                
                If Not .Text = vbCr Then
                    If Not Left(.Text, 2) = "**" Then
                    .InsertBefore "**"
                    End If
                    If Not Right(.Text, 2) = "**" Then
                    .InsertAfter "**"
                    End If
                End If
               
                .Style = ActiveDocument.Styles("Default Paragraph Font")
                .Font.Bold = False
            End With
        Loop
    End With
End Sub
 
Private Sub DokuWikiConvertItalic()
    ActiveDocument.Select
   
    With Selection.Find
   
        .ClearFormatting
        .Font.Italic = True
        .Text = ""
       
        .Format = True
        .MatchCase = False
        .MatchWholeWord = False
        .MatchWildcards = False
        .MatchSoundsLike = False
        .MatchAllWordForms = False
       
        .Forward = True
        .Wrap = wdFindContinue
       
        Do While .Execute
            With Selection
                If Len(.Text) > 1 And InStr(1, .Text, vbCr) Then
                    ' Just process the chunk before any newline characters
                    ' We'll pick-up the rest with the next search
                    .Collapse
                    .MoveEndUntil vbCr
                End If
                                      
                ' Don't bother to markup newline characters (prevents a loop, as well)
                If Not .Text = vbCr Then
                    If Not Left(.Text, 2) = "//" Then
                    .InsertBefore "//"
                    End If
                    If Not Right(.Text, 2) = "//" Then
                    .InsertAfter "//"
                    End If
                End If
               
                .Style = ActiveDocument.Styles("Default Paragraph Font")
                .Font.Italic = False
            End With
        Loop
    End With
End Sub
 
Private Sub DokuWikiConvertUnderline()
    ActiveDocument.Select
   
    With Selection.Find
   
        .ClearFormatting
        .Font.Underline = True
        .Text = ""
       
        .Format = True
        .MatchCase = False
        .MatchWholeWord = False
        .MatchWildcards = False
        .MatchSoundsLike = False
        .MatchAllWordForms = False
       
        .Forward = True
        .Wrap = wdFindContinue
       
        Do While .Execute
            With Selection
                If Len(.Text) > 1 And InStr(1, .Text, vbCr) Then
                    ' Just process the chunk before any newline characters
                    ' We'll pick-up the rest with the next search
                    .Collapse
                    .MoveEndUntil vbCr
                End If
                                       
                ' Don't bother to markup newline characters (prevents a loop, as well)
                If Not .Text = vbCr Then
                    If Not Left(.Text, 2) = "__" Then
                    .InsertBefore "__"
                    End If
                    If Not Right(.Text, 2) = "__" Then
                    .InsertAfter "__"
                    End If
                End If
                
                .Style = ActiveDocument.Styles("Default Paragraph Font")
                .Font.Underline = False
            End With
        Loop
    End With
End Sub
 
Private Sub DokuWikiConvertStrikeThrough()
    ActiveDocument.Select
   
    With Selection.Find
   
        .ClearFormatting
        .Font.StrikeThrough = True
        .Text = ""
       
        .Format = True
        .MatchCase = False
        .MatchWholeWord = False
        .MatchWildcards = False
        .MatchSoundsLike = False
        .MatchAllWordForms = False
       
        .Forward = True
        .Wrap = wdFindContinue
       
        Do While .Execute
            With Selection
                If Len(.Text) > 1 And InStr(1, .Text, vbCr) Then
                    ' Just process the chunk before any newline characters
                    ' We'll pick-up the rest with the next search
                    .Collapse
                    .MoveEndUntil vbCr
                End If
                                      
                ' Don't bother to markup newline characters (prevents a loop, as well)
                If Not .Text = vbCr Then
                    If Not Left(.Text, 2) = "<del>" Then
                    .InsertBefore "<del>"
                    End If
                    If Not Right(.Text, 2) = "</del>" Then
                    .InsertAfter "</del>"
                    End If
                End If
               
                .Style = ActiveDocument.Styles("Default Paragraph Font")
                .Font.StrikeThrough = False
            End With
        Loop
    End With
End Sub
 
Private Sub DokuWikiConvertSuperscript()
    ActiveDocument.Select
   
    With Selection.Find
   
        .ClearFormatting
        .Font.Superscript = True
        .Text = ""
       
        .Format = True
        .MatchCase = False
        .MatchWholeWord = False
        .MatchWildcards = False
        .MatchSoundsLike = False
        .MatchAllWordForms = False
       
        .Forward = True
        .Wrap = wdFindContinue
       
        Do While .Execute
            With Selection
                .Text = Trim(.Text)
                If Len(.Text) > 1 And InStr(1, .Text, vbCr) Then
                    ' Just process the chunk before any newline characters
                    ' We'll pick-up the rest with the next search
                    .Collapse
                    .MoveEndUntil vbCr
                End If
                                       
                ' Don't bother to markup newline characters (prevents a loop, as well)
                If Not .Text = vbCr Then
                    If Not Left(.Text, 2) = "<sup>" Then
                    .InsertBefore "<sup>"
                    End If
                    If Not Right(.Text, 2) = "</sup>" Then
                    .InsertAfter "</sup>"
                    End If
                End If
                
                .Style = ActiveDocument.Styles("Default Paragraph Font")
                .Font.Superscript = False
            End With
        Loop
    End With
End Sub
 
Private Sub DokuWikiConvertSubscript()
    ActiveDocument.Select
   
    With Selection.Find
   
        .ClearFormatting
        .Font.Subscript = True
        .Text = ""
       
        .Format = True
        .MatchCase = False
        .MatchWholeWord = False
        .MatchWildcards = False
        .MatchSoundsLike = False
        .MatchAllWordForms = False
       
        .Forward = True
        .Wrap = wdFindContinue
       
        Do While .Execute
            With Selection
                .Text = Trim(.Text)
                If Len(.Text) > 1 And InStr(1, .Text, vbCr) Then
                    ' Just process the chunk before any newline characters
                    ' We'll pick-up the rest with the next search
                    .Collapse
                    .MoveEndUntil vbCr
                End If
                                       
                ' Don't bother to markup newline characters (prevents a loop, as well)
                If Not .Text = vbCr Then
                    If Not Left(.Text, 2) = "<sub>" Then
                    .InsertBefore "<sub>"
                    End If
                    If Not Right(.Text, 2) = "</sub>" Then
                    .InsertAfter "</sub>"
                    End If
                End If
               
                .Style = ActiveDocument.Styles("Default Paragraph Font")
                .Font.Subscript = False
            End With
        Loop
    End With
End Sub
 
Private Sub DokuWikiConvertLists()
    Dim para As Paragraph
    For Each para In ActiveDocument.ListParagraphs
        With para.Range
            .InsertBefore "  "
             If .ListFormat.ListType = wdListBullet Then
                 .InsertBefore "*"
             Else
                  .InsertBefore "-"
              End If
            For i = 1 To .ListFormat.ListLevelNumber
                   .InsertBefore "  "
           Next i
            .ListFormat.RemoveNumbers
        End With
    Next para
End Sub
 
Private Sub DokuWikiConvertHyperlinks()
    Dim hyperCount As Integer
   
    hyperCount = ActiveDocument.Hyperlinks.Count
   
    For i = 1 To hyperCount
        With ActiveDocument.Hyperlinks(1)
            Dim addr As String
            addr = .Address
            .Delete
            .Range.InsertBefore "["
            .Range.InsertAfter "-" & addr & "]"
        End With
    Next i
End Sub
 
' Replace all smart quotes with their dumb equivalents
Private Sub ReplaceQuotes()
    Dim quotes As Boolean
    quotes = Options.AutoFormatAsYouTypeReplaceQuotes
    Options.AutoFormatAsYouTypeReplaceQuotes = False
    ReplaceString ChrW(8220), """"
    ReplaceString ChrW(8221), """"
    ReplaceString "ë", "'"
    ReplaceString "í", "'"
    Options.AutoFormatAsYouTypeReplaceQuotes = quotes
End Sub
 
Private Sub DokuWikiEscapeChars()
    EscapeCharacter "*"
    EscapeCharacter "#"
    EscapeCharacter "_"
    EscapeCharacter "-"
    EscapeCharacter "+"
    EscapeCharacter "{"
    EscapeCharacter "}"
    EscapeCharacter "["
    EscapeCharacter "]"
    EscapeCharacter "~"
    EscapeCharacter "^^"
    EscapeCharacter "|"
    EscapeCharacter "'"
End Sub
 
Private Function ReplaceHeading(styleHeading As String, headerPrefix As String)
    Dim normalStyle As Style
    Set normalStyle = ActiveDocument.Styles(wdStyleNormal)
   
    ActiveDocument.Select
   
    With Selection.Find
   
        .ClearFormatting
        .Style = ActiveDocument.Styles(styleHeading)
        .Text = ""

      
        .Format = True
        .MatchCase = False
        .MatchWholeWord = False
        .MatchWildcards = False
        .MatchSoundsLike = False
        .MatchAllWordForms = False
       
        .Forward = True
        .Wrap = wdFindContinue
       
        Do While .Execute
            With Selection
                If InStr(1, .Text, vbCr) Then
                    ' Just process the chunk before any newline characters
                    ' We'll pick-up the rest with the next search
                    .Collapse
                    .MoveEndUntil vbCr
                End If
                                       
                ' Don't bother to markup newline characters (prevents a loop, as well)
               If Not .Text = vbCr Then
                   .InsertBefore headerPrefix
                   .InsertBefore vbCr
                   .InsertAfter headerPrefix
               End If
               .Style = normalStyle
           End With
       Loop
   End With
End Function

Private Sub DokuWikiConvertTable()
Dim TotTables As Long
Do While ActiveDocument.Tables.Count() > 0
ActiveDocument.Tables(1).Range.Select
Selection.Find.ClearFormatting
Selection.Find.Replacement.ClearFormatting
With Selection.Find
.Text = " $s$|$s$ "
.Replacement.Text = "I"
.Forward = True
.Wrap = wdFindContinue
.Format = False
.MatchCase = False
.MatchWholeWord = False
.MatchWildcards = False
.MatchSoundsLike = False
.MatchAllWordForms = False
End With
Selection.Find.Execute Replace:=wdReplaceAll
Selection.Find.ClearFormatting
Selection.Find.Replacement.ClearFormatting
With Selection.Find
.Text = " $s$^^$s$ "
.Replacement.Text = "/\"
.Forward = True
.Wrap = wdFindContinue
.Format = False
.MatchCase = False
.MatchWholeWord = False
.MatchWildcards = False
.MatchSoundsLike = False
.MatchAllWordForms = False
End With
Selection.Find.Execute Replace:=wdReplaceAll
Selection.Find.ClearFormatting
Application.DefaultTableSeparator = "|"
Selection.Rows.ConvertToText Separator:=wdSeparateByDefaultListSeparator, NestedTables:=True
Selection.Find.ClearFormatting
Selection.Find.Replacement.ClearFormatting
With Selection.Find
.Text = "^p"
.Replacement.Text = "|^p|"
.Forward = True
.Wrap = wdFindStop
.Format = False
.MatchCase = False
.MatchWholeWord = False
.MatchWildcards = False
.MatchSoundsLike = False
.MatchAllWordForms = False
End With
Selection.Find.Execute Replace:=wdReplaceAll
Selection.InsertBefore ("|")
Selection.InsertParagraphAfter
Selection.Find.ClearFormatting
Selection.Find.Replacement.ClearFormatting
With Selection.Find
.Text = "^p|^p"
.Replacement.Text = "^p"
.Forward = True
.Wrap = wdFindStop
.Format = False
.MatchCase = False
.MatchWholeWord = False
.MatchWildcards = False
.MatchSoundsLike = False
.MatchAllWordForms = False
End With
Selection.Find.Execute Replace:=wdReplaceAll
Selection.Find.ClearFormatting
Selection.Find.Replacement.ClearFormatting
With Selection.Find
.Text = "$s$blank$s$"
.Replacement.Text = ""
.Forward = True
.Wrap = wdFindContinue
.Format = False
.MatchCase = False
.MatchWholeWord = False
.MatchWildcards = False
.MatchSoundsLike = False
.MatchAllWordForms = False
End With
Selection.Find.Execute Replace:=wdReplaceAll
Selection.Find.ClearFormatting
Selection.Find.Replacement.ClearFormatting
With Selection.Find
.Text = "||"
.Replacement.Text = "|  |"
.Forward = True
.Wrap = wdFindStop
.Format = False
.MatchCase = False
.MatchWholeWord = False
.MatchWildcards = False
.MatchSoundsLike = False
.MatchAllWordForms = False
End With
Selection.Find.Execute Replace:=wdReplaceAll
With Selection.Find
.Text = "||"
.Replacement.Text = "|  |"
.Forward = True
.Wrap = wdFindStop
.Format = False
.MatchCase = False
.MatchWholeWord = False
.MatchWildcards = False
.MatchSoundsLike = False
.MatchAllWordForms = False
End With
Selection.Find.Execute Replace:=wdReplaceAll
Selection.Find.ClearFormatting
Selection.Find.Replacement.ClearFormatting
With Selection.Find
.Text = "| |"
.Replacement.Text = "|  |"
.Forward = True
.Wrap = wdFindStop
.Format = False
.MatchCase = False
.MatchWholeWord = False
.MatchWildcards = False
.MatchSoundsLike = False
.MatchAllWordForms = False
End With
Selection.Find.Execute Replace:=wdReplaceAll
With Selection.Find
.Text = "| |"
.Replacement.Text = "|  |"
.Forward = True
.Wrap = wdFindStop
.Format = False
.MatchCase = False
.MatchWholeWord = False
.MatchWildcards = False
.MatchSoundsLike = False
.MatchAllWordForms = False
End With
Selection.Find.Execute Replace:=wdReplaceAll
Selection.Paragraphs(1).Range.Select
Selection.Find.ClearFormatting
Selection.Find.Replacement.ClearFormatting
With Selection.Find
.Text = "|"
.Replacement.Text = "^^"
.Forward = True
.Wrap = wdFindStop
.Format = False
.MatchCase = False
.MatchWholeWord = False
.MatchWildcards = False
.MatchSoundsLike = False
.MatchAllWordForms = False
End With
Selection.Find.Execute Replace:=wdReplaceAll
Loop
End Sub
Private Sub UndoDokuWikiEscapeChars()

    UndoEscapeCharacter "*"
    UndoEscapeCharacter "#"
    UndoEscapeCharacter "_"
    UndoEscapeCharacter "-"
    UndoEscapeCharacter "+"
    UndoEscapeCharacter "{"
    UndoEscapeCharacter "}"
    UndoEscapeCharacter "["
    UndoEscapeCharacter "]"
    UndoEscapeCharacter "~"
    UndoEscapeCharacter "^^"
    UndoEscapeCharacter "|"
    UndoEscapeCharacter "'"

End Sub

Private Function EscapeCharacter(char As String)
    ReplaceString char, " $s$" & char & "$s$ "
End Function

Private Function UndoEscapeCharacter(char As String)
    ReplaceString " $s$" & char & "$s$ ", char
End Function

Private Function ReplaceString(findStr As String, replacementStr As String)
    Selection.Find.ClearFormatting
    Selection.Find.Replacement.ClearFormatting
    With Selection.Find
        .Text = findStr
        .Replacement.Text = replacementStr
        .Forward = True
        .Wrap = wdFindContinue
        .Format = False
        .MatchCase = False
        .MatchWholeWord = False
        .MatchWildcards = False
        .MatchSoundsLike = False
        .MatchAllWordForms = False
    End With
    Selection.Find.Execute Replace:=wdReplaceAll
End Function
</code>