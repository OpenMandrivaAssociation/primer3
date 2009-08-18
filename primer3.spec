%define name	primer3
%define version 1.1.4
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	PCR reactions primers identification
Group:		Sciences/Biology
License:	BSD like
URL:		http://primer3.sourceforge.net/
Source0:	http://downloads.sourceforge.net/primer3/%{name}-%{version}.tar.bz2
Patch0:		format_arguments_fix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Primer3 is a complete rewrite of the original PRIMER program
(Primer 0.5), written by Steve Lincoln, Mark Daly, and Eric
Lander.

Primer3 picks primers for PCR reactions, considering as criteria:
- oligonucleotide melting temperature, size, GC content,
  and primer-dimer possibilities
- PCR product size
- positional constraints within the source sequence
- miscellaneous other constraints
All of these criteria are user-specifiable as constraints, and
some are specifiable as terms in an objective function that
characterizes an optimal primer pair.

%prep
%setup -q -n %{name}-%{version}
chmod 644  COPYING.txt README.txt example

%patch0 -p1

%build
cd src && %make CFLAGS="$RPM_OPT_FLAGS" LIBOPTS=""

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 src/primer3_core %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING.txt README.txt example src/release_notes.txt
%{_bindir}/primer3_core

