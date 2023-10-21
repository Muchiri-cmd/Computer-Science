Imports System.Drawing.Text

Public Class Form1
    Private Sub btnHello_Click(sender As Object, e As EventArgs) Handles btnHello.Click
        Dim icount As Integer
        Dim stOut As String

        For icount = 1 To 10
            stOut = stOut & "hello world " & icount & System.Environment.NewLine


        Next icount

        MsgBox(stOut)



    End Sub
End Class
