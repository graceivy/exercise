# --- alb/main.tf ---

resource "aws_lb" "mtc_lb" {
  name            = "mtc-loadbalancer"
  security_groups = var.public_sg
  subnets         = var.public_subnets

  idle_timeout = 400
}

resource "aws_lb_target_group" "mtc_tg" {
  name     = "mtc-lb-tg-${substr(uuid(), 0, 3)}"
  port     = var.tg_port     #80
  protocol = var.tg_protocol #"HTTP"
  vpc_id   = var.vpc_id
  health_check {
    healthy_threshold   = var.lb_healthy_threshold   #2
    unhealthy_threshold = var.lb_unhealthy_threshold #2
    timeout             = var.lb_timeout             #3
    interval            = var.lb_interval            #30
  }

  # When terraform apply every time, the uuid is different so the target group will be destroyed and created again.
  # So the listener is going to be migrated to the new target group. But as the tg is destroyed first and the 
  # listen has not any target group to be migrated yet, so the destroy of the old tg won't be successful.
  # So we use ignore_changes to avoid the terraform to create a new tg
  # Another way to do is to use create_before_destroy. For example if the port changes.

  lifecycle {
    ignore_changes        = [name]
    create_before_destroy = true
  }
}

resource "aws_lb_listener" "mte_lb_listener" {
  load_balancer_arn = aws_lb.mtc_lb.arn
  port              = var.listener_port     #"80"
  protocol          = var.listener_protocol #"HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.mtc_tg.arn
  }
}