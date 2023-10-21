Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim icount As Integer

        Do While icount <= 5
            MsgBox("Hello " & icount)
        Loop
    End Sub
End Class
