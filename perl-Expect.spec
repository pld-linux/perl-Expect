%include	/usr/lib/rpm/macros.perl
Summary:	Expect perl module
Summary(pl):	Modu³ perla Expect
Name:		perl-Expect
Version:	1.07
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module//Expect.pm-%{version}.tar.gz
Patch:		perl-Expect-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-IO-Stty
BuildRequires:	perl-IO-Tty
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Expect perl module.

%description -l pl
Modu³ perla Expect.

%prep
%setup -q -n Expect.pm-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Expect
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README FAQ

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,FAQ}.gz tutorial

%{perl_sitelib}/Expect.pm
%{perl_sitelib}/term-filter.pl
%{perl_sitearch}/auto/Expect

%{_mandir}/man3/*
