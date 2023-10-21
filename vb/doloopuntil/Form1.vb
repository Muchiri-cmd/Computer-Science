Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim iCount As Integer

        Do
            iCount = iCount + 1
            MsgBox("hello " & iCount)

        Loop Until iCount = 5
        MsgBox("all done ")
    End Sub
End Class
