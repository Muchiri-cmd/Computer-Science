Public Class Form1
    Private Function Soduku(urefu As Double, upana As Double, kimo As Double)
        MessageBox.Show("Box " & vbCrLf & "width= " & "length= " & upana & vbCrLf & "Height = " &
                        kimo & vbCrLf & "Its volume is " & urefu * upana * kimo)
    End Function

    Private Sub btnBox_Click(sender As Object, e As EventArgs) Handles btnBox.Click
        Dim l As Double, w As Double, h As Double
        l = InputBox("Enter length ")
        w = InputBox("Enter width ")
        h = InputBox("Enter height ")

        Call Soduku(l, w, h)
        Call Soduku(10, 6, 3)
        Call Soduku(100, 60, 20)
        Call Soduku(12, 20, 10)
    End Sub
End Class
