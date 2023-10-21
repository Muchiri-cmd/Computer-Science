Public Class Form1
    Private Sub btnGetGrade_Click(sender As Object, e As EventArgs) Handles btnGetGrade.Click
        Dim iScore As Integer

        If IsNumeric(txtExamScore.Text) = True Then
            iScore = CInt(txtExamScore.Text)
        Else
            MsgBox("You must enter a number")
            Exit Sub
        End If

        ' if iscore ,0 or iscore>=100 Then
        If Not (iScore > 0 Or iScore <= 100) Then
            MsgBox("Invalid score. Enter valid number")
            Exit Sub
        ElseIf iScore <= 20 Then
            MsgBox("GRADE F")
        ElseIf iScore > 20 And iScore <= 30 Then
            MsgBox("GRADE E")
        ElseIf iScore > 30 And iScore <= 40 Then
            MsgBox("GRADE D")
        ElseIf iScore > 40 And iScore <= 50 Then
            MsgBox("GRADE C")
        ElseIf iScore > 50 And iScore <= 70 Then
            MsgBox("GRADE B")
        Else
            MsgBox("GRADE A")
        End If
    End Sub
End Class
