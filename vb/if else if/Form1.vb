Public Class Form1
    Private Sub btnGreetings_Click(sender As Object, e As EventArgs) Handles btnGreetings.Click
        Dim stCountry As String

        stCountry = txtCountry.Text
        stCountry = stCountry.ToLower

        If stCountry = "australia" Then
            MsgBox("G'day Mate,good on ya")
        ElseIf stCountry = "france" Then
            MsgBox("Bonjour,comment allez-vouz")
        ElseIf stCountry = "kenya" Then
            MsgBox("Karibu,hakuna matata")
        Else
            MsgBox("Welcome to Kuvuki land")
        End If



    End Sub
End Class
