#
#   - DBI -
#   This spec file was automatically generated by cpan2rpm [ver: 2.028]
#   The following arguments were used:
#       /opt/freeware/src/packages/SOURCES/DBI-1.611.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define pkgname DBI
%define filelist %{pkgname}-%{version}-filelist
%define NVR %{pkgname}-%{version}-%{release}
%define maketest 1

name:      perl-DBI
summary:   DBI - Database independent interface for Perl
version:   1.611
release:   1
vendor:    Tim Bunce (dbi-users@perl.org)
packager:  Arix International <cpan2rpm@arix.com>
license:   Artistic
group:     Applications/CPAN
url:       http://www.cpan.org
buildroot: %{_tmppath}/%{name}-%{version}-%(id -u -n)
buildarch: ppc
prefix:    %(echo %{_prefix})
source:    DBI-1.611.tar.gz

%description
The DBI is a database access module for the Perl programming language.  It defines
a set of methods, variables, and conventions that provide a consistent
database interface, independent of the actual database being used.

It is important to remember that the DBI is just an interface.
The DBI is a layer
of "glue" between an application and one or more database *driver*
modules.  It is the driver modules which do most of the real work. The DBI
provides a standard interface and framework for the drivers to operate
within.

#
# This package was generated automatically with the cpan2rpm
# utility.  To get this software or for more information
# please visit: http://perl.arix.com/
#

%prep
%setup -q -n %{pkgname}-%{version} 
chmod -R u+w %{_builddir}/%{pkgname}-%{version}

%build
grep -rsl '^#!.*perl' . |
#   grep -v '.bak$' |xargs --no-run-if-empty \
grep -v '.bak$' |xargs \
%__perl -MExtUtils::MakeMaker -e 'MY->fixin(@ARGV)'
CFLAGS="$RPM_OPT_FLAGS"
%{__perl} Makefile.PL `%{__perl} -MExtUtils::MakeMaker -e ' print qq|PREFIX=%{buildroot}%{_prefix}| if \$ExtUtils::MakeMaker::VERSION =~ /5\.9[1-6]|6\.0[0-5]/ '`
%{__make} 
%if %maketest
%{__make} test
%endif

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%{makeinstall} `%{__perl} -MExtUtils::MakeMaker -e ' print \$ExtUtils::MakeMaker::VERSION <= 6.05 ? qq|PREFIX=%{buildroot}%{_prefix}| : qq|DESTDIR=%{buildroot}| '`

cmd=/usr/share/spec-helper/compress_files
[ -x $cmd ] || cmd=/usr/lib/rpm/brp-compress
[ -x $cmd ] && $cmd

# SuSE Linux
#        if [ -e /etc/SuSE-release -o -e /etc/UnitedLinux-release ]
#        then
#            %{__mkdir_p} %{buildroot}/var/adm/perl-modules
#            %{__cat} `find %{buildroot} -name "perllocal.pod"`  \
#                | %{__sed} -e s+%{buildroot}++g                 \
#                > %{buildroot}/var/adm/perl-modules/%{name}
#        fi

# remove special files
find %{buildroot} -name "perllocal.pod" \
    -o -name ".packlist"                \
    -o -name "*.bs"                     \
    |xargs -i rm -f {}

# no empty directories
#        find %{buildroot}%{_prefix}             \
#            -type d -depth                      \
#            -exec rmdir {} \; 2>/dev/null

%{__perl} -MFile::Find -le '
    find({ wanted => \&wanted, no_chdir => 1}, "%{buildroot}");
    print "%doc  TODO_2005.txt ex Changes TODO_gofer.txt README";
    for my $x (sort @dirs, @files) {
        push @ret, $x unless indirs($x);
        }
    print join "\n", sort @ret;

    sub wanted {
        return if /auto$/;

        local $_ = $File::Find::name;
        my $f = $_; s|^\Q%{buildroot}\E||;
        return unless length;
        return $files[@files] = $_ if -f $f;

        $d = $_;
        /\Q$d\E/ && return for reverse sort @INC;
        $d =~ /\Q$_\E/ && return
            for qw|/etc %_prefix/man %_prefix/bin %_prefix/share|;

        $dirs[@dirs] = $_;
        }

    sub indirs {
        my $x = shift;
        $x =~ /^\Q$_\E\// && $x ne $_ && return 1 for @dirs;
        }
    ' > %filelist

[ -z %filelist ] && {
    echo "ERROR: empty %files listing"
    exit -1
    }

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %filelist
%defattr(-,root,root)

%changelog
* Wed Jun 16 2010 root@c114m4h1p04.ppd.pok.ibm.com
- Initial build.