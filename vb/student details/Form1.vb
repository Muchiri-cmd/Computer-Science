Public Class Form1
    Private Sub btnRecord_Click(sender As Object, e As EventArgs) Handles btnRecord.Click
        Dim stFirstName As String
        Dim stSecondName As String
        Dim stRegNo As String
        Dim stOccupation As String

        stFirstName = txtFirstName.Text
        stSecondName = txtSecondName.Text
        stRegNo = txtRegNo.Text
        stOccupation = lstCourse.Text

        MsgBox(stFirstName & " " & stSecondName & " " & stRegNo & " is pursuing " & stOccupation)


    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        lstCourse.Items.Add("Computer Forensics")
        lstCourse.Items.Add("Information Security")
        lstCourse.Items.Add("Cybersecurity")
    End Sub
End Class
