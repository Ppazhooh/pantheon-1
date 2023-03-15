#!/usr/bin/env python

from os import path
from subprocess import check_call

import arg_parser
import context
from helpers import utils


def main():
    args = arg_parser.sender_first()

    cc_repo = path.join(context.third_party_dir, 'DeepCC/deepcc.v1.0')
    model_repo = path.join(context.third_party_dir, 'DeepCC/models')
    send_src = path.join(cc_repo, 'rl-module', 'rl-server')
    recv_src = path.join(cc_repo, 'rl-module', 'client')

    if args.option == 'deps':
        print 'libtbb-dev libasio-dev libalglib-dev libboost-system-dev'
        return

    if args.option == 'setup':
        utils.apply_patch('deepcc.patch', cc_repo)
        sh_cmd = './build.sh'
        model_cmd = './setitup.sh'
        check_call(sh_cmd, shell=True, cwd=cc_repo)
        check_call(model_cmd, shell=True, cwd=model_repo)
        return

    if args.option == 'receiver':
        cmd = [recv_src, args.ip , '1', args.port]
        check_call(cmd, cwd=utils.tmp_dir)
        return




    if args.option == 'sender':
        target = '60'
        initial_alpha = '150'
        period = '20'

        cmd = [send_src, '0',args.port, '0' , '150', '500',target, initial_alpha,'500', period, '2', '2','cubic']
        check_call(cmd, cwd=utils.tmp_dir)
        return



if __name__ == '__main__':
    main()
