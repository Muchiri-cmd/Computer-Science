Public Class Form1
    Private Sub btnCalculate_Click(sender As Object, e As EventArgs) Handles btnCalculate.Click
        Dim dbFirstNumber As Double
        Dim dbSecondNumber As Double
        Dim dbResult As Double

        dbFirstNumber = txtNumber1.Text
        dbSecondNumber = txtNumber2.Text
        dbResult = dbFirstNumber Mod dbSecondNumber
        MsgBox("The result is " & dbResult)

    End Sub
End Class
