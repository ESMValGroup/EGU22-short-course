import sys
import sh
import os
from dataclasses import dataclass


@dataclass
class Account:
    host: str
    user: str
    password: str

    def run(self, *cmd):
        """Run `cmd` remotely."""
        sh.sshpass(
            "-p",
            self.password,
            "ssh",
            "-o",
            "PreferredAuthentications=password",
            "-o",
            "PubkeyAuthentication=no",
            f"{self.user}@{self.host}",
            *cmd,
        )

    def copy(self, src, tgt):
        """Copy `src` to `tgt`."""
        dirname = os.path.dirname(tgt)
        if dirname:
            self.run(
                "mkdir",
                "-p",
                dirname,
            )
        sh.rsync(
            "-e",
            f"sshpass -p '{self.password}' ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no",
            src,
            f"{self.user}@{self.host}:{tgt}",
        )


def main(password):
    # host = "mistral.dkrz.de"
    host = "levante.dkrz.de"
    # accounts = ["k206102"]  # single account for testing
    accounts = [f"k206{i}" for i in range(103, 120)]
    for user in accounts:
        account = Account(host, user, password)
        account.copy(
            src="config-user-v2.5-levante.yml",
            tgt=".esmvaltool/config-user.yml",
        )
        account.copy(
            src="environment_versions.yml",
            tgt="environment_versions.yml",
        )
        account.run(
            [
                " && ".join(
                    [
                        ". /sw/spack-levante/mambaforge-4.11.0-0-Linux-x86_64-sobz6z/etc/profile.d/conda.sh",
                        ". /sw/spack-levante/mambaforge-4.11.0-0-Linux-x86_64-sobz6z/etc/profile.d/mamba.sh",
                        "mamba env create -q -n esmvaltool -f environment_versions.yml",
                        "conda run -n esmvaltool python -m ipykernel install --user --name ESMValTool",
                        "rm environment_versions.yml",
                    ]
                )
            ]
        )


if __name__ == "__main__":

    main(sys.argv[1])
