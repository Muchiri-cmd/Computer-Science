Public Class Form1
    Private Function FindAvg(x As Double, Y As Double, z As Double)
        'Return/FindAvg =
        FindAvg = (x * Y * z) / 3
    End Function

    Private Sub btnNumbers_Click(sender As Object, e As EventArgs) Handles btnNumbers.Click
        Dim NumYangu As Double, NumYake As Double, NumYao As Double, Mean As Double
        NumYangu = InputBox("Enter your number ")
        NumYake = InputBox("Enter her number ")
        NumYao = InputBox("Enter their number ")
        Mean = FindAvg(NumYangu, NumYake, NumYao)
        MessageBox.Show("The numbers are " & NumYangu & " ," & NumYake & " and " & NumYao & vbCrLf & "Their mean is " & Mean)

    End Sub
End Class
