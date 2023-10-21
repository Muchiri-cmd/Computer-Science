Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim icount As Integer = 0

        Do While icount < 5
            icount = icount + 1
            MsgBox("hello world " & icount)
        Loop
        MsgBox("all done ")

        Do
            icount = icount + 1
            MsgBox("hello world " & icount)

        Loop While icount < 10
    End Sub
End Class
