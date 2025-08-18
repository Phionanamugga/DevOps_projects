provider "aws" { region = "eu-central-1" }
resource "aws_launch_template" "web" {
  name_prefix   = "demo-web-"
  image_id      = "ami-12345678" # Replace with valid AMI
  instance_type = "t2.micro"
}
resource "aws_autoscaling_group" "asg" {
  desired_capacity = 2
  max_size         = 3
  min_size         = 1
  vpc_zone_identifier = ["subnet-123456"]
  launch_template {
    id      = aws_launch_template.web.id
    version = "$Latest"
  }
}
resource "aws_lb" "web_lb" {
  name               = "demo-lb"
  load_balancer_type = "application"
  subnets            = ["subnet-123456"]
}
