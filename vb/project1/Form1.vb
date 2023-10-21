Public Class Form1
    Private Sub btnStart_Click(sender As Object, e As EventArgs) Handles btnStart.Click
        MsgBox("Greetings.This is Fsociety")
        MsgBox("your files have been encrypted.")
        MsgBox("pay to 0113708866 MPESA to get the decryption key")
        MessageBox.Show("Privacy is a myth")
    End Sub

    Private Sub btnVar_Click(sender As Object, e As EventArgs) Handles btnVar.Click
        Dim stFirstName As String
        stFirstName = "chepuu"
        MsgBox("welcome to vb " & stFirstName)
    End Sub

    Private Sub btnDatatypes_Click(sender As Object, e As EventArgs) Handles btnDatatypes.Click
        Dim stName As String
        Dim iAge As Integer
        Dim dFeeBalance As Decimal
        Dim bReported As Boolean
        Dim dReportingDay As Date

        stName = "Chepuu"
        iAge = 18
        dFeeBalance = 999.0
        bReported = True
        dReportingDay = #01/07/2023#

        MsgBox(stName & vbNewLine &
               iAge & vbNewLine &
               dFeeBalance & vbNewLine &
               bReported & vbNewLine &
               dReportingDay)
    End Sub

    Private Sub btnInput_Click(sender As Object, e As EventArgs) Handles btnInput.Click
        Dim stFirstName As String
        Dim iAge As Integer


        stFirstName = InputBox("enter your first name")
        iAge = InputBox("enter age")

        MessageBox.Show("name: " & stFirstName & vbNewLine & "years: " & iAge & " " & stOccupation)



    End Sub

    Private Sub btnSum_Click(sender As Object, e As EventArgs) Handles btnCalculate.Click
        Dim iFirstNumber As Integer
        Dim iSecondNumber As Integer

        iFirstNumber = txtFirstNumber.Text
        iSecondNumber = txtSecondNumber.Text
        txtDisplaySum.Text = Val(txtFirstNumber.Text) + Val(txtSecondNumber.Text)

    End Sub

    Private Sub lstEngineering_SelectedIndexChanged(sender As Object, e As EventArgs) 
        Dim course
    End Sub
End Class
