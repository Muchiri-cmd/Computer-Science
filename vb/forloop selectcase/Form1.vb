Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim i As Integer
        For i = 1 To 10
            Select Case i
                Case 1
                    MsgBox("The value is 1")
                Case 2
                    MsgBox("The value is 2")
                Case Else
                    MsgBox("Not 1 or 2 ")
            End Select
        Next i
    End Sub
End Class
