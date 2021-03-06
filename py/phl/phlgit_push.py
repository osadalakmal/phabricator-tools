"""Wrapper around 'git push'"""
# =============================================================================
# CONTENTS
# -----------------------------------------------------------------------------
# phlgit_push
#
# Public Functions:
#   push_asymmetrical_force
#   push_asymmetrical
#   push
#   move_asymmetrical
#   delete
#
# -----------------------------------------------------------------------------
# (this contents block is generated, edits will be lost)
# =============================================================================


def push_asymmetrical_force(clone, localBranch, remoteBranch, remoteName):
    clone.call('push', remoteName, localBranch + ":" + remoteBranch, "--force")


def push_asymmetrical(clone, localBranch, remoteBranch, remoteName):
    clone.call('push', remoteName, localBranch + ":" + remoteBranch)


def push(clone, branch, remoteName):
    clone.call('push', remoteName, branch)


def move_asymmetrical(clone, local_branch, old_remote, new_remote, remote):
    """Delete 'old_remote', push 'local_branch' to 'new_remote' on 'remote'.

    :clone: supports call()
    :local_branch: the local reference to push
    :old_remote: the old reference on the remote to delete
    :new_remote: the new reference on the remote to push to
    :remote: the name of the remote to push to
    :returns: None

    """
    clone.call(
        'push',
        remote,
        local_branch + ":" + new_remote,
        ":" + old_remote)


def delete(clone, branch, remote):
    """Delete 'branch' from the specified remote.

    :clone: supports call()
    :branch: string name of the branch
    :remote: string name of the remote
    :returns: None

    """
    clone.call('push', remote, ":" + branch)

#------------------------------------------------------------------------------
# Copyright (C) 2012 Bloomberg L.P.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#------------------------------- END-OF-FILE ----------------------------------
